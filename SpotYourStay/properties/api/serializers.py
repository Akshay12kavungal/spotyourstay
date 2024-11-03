# properties/serializers.py

from rest_framework import serializers
from properties.models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id', 'name', 'description', 'location', 'price_per_night', 'availability', 
            'highlights', 'spaces', 'amenities', 'meals', 'location_details', 'experiences', 
            'faqs', 'photos', 'owner'
        ]
        read_only_fields = ['id', 'owner']
