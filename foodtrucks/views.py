import json
from typing import Dict

from django.contrib.gis.db.models.functions import Distance
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.geos import Point
from django.views.generic import ListView
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView

from foodtrucks.models import FoodTruck
from foodtrucks.serializers import FoodTruckListSerializer


class NearByFoodTruckListMixin:
    """
    Mixin for filtering and providing nearby food truck functionality.
    """

    def get_queryset(self):
        """
        Get the queryset of nearby food trucks based on the provided latitude and longitude.

        Retrieves the nearest food trucks using the `get_nearby_locations` method.

        Returns:
            QuerySet: A queryset of FoodTruck objects ordered by proximity to the given location.
        """
        try:
            required_parameters = {
                'lat': self.request.query_params.get('lat', None),
                'lng': self.request.query_params.get('lng', None),
            }
        except Exception:
            required_parameters = self.request.GET.dict()
        self.__validate_get_params(required_parameters)
        return self.get_nearby_locations(float(required_parameters['lat']), float(required_parameters['lng']))

    @staticmethod
    def get_nearby_locations(latitude: float, longitude: float, max_results: int = 5):
        """
        Retrieve a list of nearby food trucks based on latitude and longitude.

        Args:
            latitude (float): Latitude of the location.
            longitude (float): Longitude of the location.
            max_results (int): Maximum number of results to return.

        Returns:
            QuerySet: A queryset of FoodTruck objects annotated with distance from the given location,
                      ordered by ascending distance.
        """

        # Create a Point object from the given latitude and longitude
        user_location = Point(longitude, latitude, srid=4326)

        # Query the database for the nearest locations
        return FoodTruck.objects.annotate(
            distance=Distance('location', user_location)
        ).order_by('distance')[:max_results]

    @staticmethod
    def __validate_get_params(params: Dict):
        """
        Validate the required query parameters.

        Args:
            params (dict): A dictionary of query parameters with their values.

        Raises:
            ValidationError: If any required parameter is missing or empty.
        """
        errors = {}
        for parameter in params:
            if not params[parameter]:
                errors[parameter] = _('This parameter is required.')
        if errors:
            raise ValidationError(errors)


class NearByFoodTruckListAPIView(NearByFoodTruckListMixin, ListAPIView):
    """
    API view for listing nearby food trucks.
    """

    queryset = FoodTruck.objects.all()
    serializer_class = FoodTruckListSerializer


class NearByFoodTruckListTemplateView(NearByFoodTruckListMixin, ListView):
    """
    Template view for displaying nearby food trucks on a map.
    template_name = 'foodtrucks/index.html'
    """

    model = FoodTruck

    def get_context_data(self, **kwargs):
        """
        Add JSON list of food trucks to the context.
        """
        context = super().get_context_data(**kwargs)
        # Get the queryset of food trucks
        queryset = self.get_queryset()
        # Serialize the queryset
        food_trucks = FoodTruckListSerializer(instance=queryset, many=True).data
        # Dump the JSON list to the context
        context['food_trucks'] = json.dumps(food_trucks)
        return context
