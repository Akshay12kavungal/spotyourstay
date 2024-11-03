# properties/models.py

from django.db import models
from django.conf import settings

class Property(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    highlights = models.TextField()
    spaces = models.TextField()
    amenities = models.JSONField()  # Store amenities as a JSON array
    meals = models.TextField()
    location_details = models.TextField()
    experiences = models.TextField()
    faqs = models.JSONField()  # Store FAQs as a JSON array
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)  # Track if property is available
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to User
    photos = models.ImageField(upload_to='property_photos/', blank=True, null=True)  # Handle photo uploads

    def __str__(self):
        return self.name
