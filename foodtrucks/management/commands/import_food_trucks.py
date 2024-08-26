import csv
from django.core.management.base import BaseCommand
from foodtrucks.models import FoodTruck
from django.contrib.gis.geos import Point
from datetime import datetime


class Command(BaseCommand):
    help = 'Import locations from CSV'

    def handle(self, *args, **kwargs):
        file_path = 'food-truck-data.csv'
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')  # Assuming tab-delimited CSV
            for row in reader:
                # Convert the necessary fields to the correct data type
                latitude = float(row['Latitude'])
                longitude = float(row['Longitude'])
                location_point = Point(longitude, latitude, srid=4326)

                approved = datetime.strptime(row['Approved'], '%m/%d/%Y %I:%M:%S %p') if row['Approved'] else None
                received = datetime.strptime(row['Received'], '%Y%m%d') if row['Received'] else None
                expiration_date = datetime.strptime(row['ExpirationDate'], '%m/%d/%Y %I:%M:%S %p') if row[
                    'ExpirationDate'] else None

                # Create or update the Location object
                FoodTruck.objects.update_or_create(
                    applicant=row['Applicant'],
                    defaults={
                        'facility_type': row['FacilityType'],
                        'location_description': row['LocationDescription'],
                        'address': row['Address'],
                        'status': row['Status'],
                        'food_items': row['FoodItems'],
                        'location': location_point,
                        'dayshours': row['dayshours'],
                        'approved': approved,
                        'received': received,
                        'expiration_date': expiration_date,
                    }
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported locations'))
