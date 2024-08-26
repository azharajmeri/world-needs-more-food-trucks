from rest_framework import serializers

from foodtrucks.models import FoodTruck


class FoodTruckListSerializer(serializers.ModelSerializer):
    """
    Serializer for the FoodTruck model.

    This serializer is used to convert FoodTruck instances to JSON format and vice versa.
    It includes all fields from the FoodTruck model.
    """

    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    class Meta:
        model = FoodTruck
        fields = '__all__'

    def get_latitude(self, obj):
        return obj.latitude

    def get_longitude(self, obj):
        return obj.longitude