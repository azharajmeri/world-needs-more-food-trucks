# Generated by Django 5.1 on 2024-08-26 10:58

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.CharField(max_length=255)),
                ('cnn', models.CharField(max_length=255)),
                ('facility_type', models.CharField(max_length=100)),
                ('location_description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=100)),
                ('food_items', models.TextField()),
                ('location', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('dayshours', models.CharField(max_length=100)),
                ('approved', models.DateField(blank=True, null=True)),
                ('received', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
