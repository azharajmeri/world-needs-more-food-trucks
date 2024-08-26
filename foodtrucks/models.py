from django.contrib.gis.db.models import PointField
from django.db import models


class FoodTruck(models.Model):
    applicant = models.CharField(max_length=255)
    cnn = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=100)
    location_description = models.TextField()
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    food_items = models.TextField()
    location = PointField(geography=True, srid=4326)  # SRID 4326 is for WGS84
    dayshours = models.CharField(max_length=100)
    approved = models.DateField(null=True, blank=True)
    received = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.applicant} - {self.facility_type}"

    @property
    def latitude(self):
        return self.location.y

    @property
    def longitude(self):
        return self.location.x
