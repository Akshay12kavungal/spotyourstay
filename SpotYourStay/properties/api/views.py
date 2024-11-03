# properties/api/views.py

from rest_framework import generics
from ..models import Property  # Adjust based on your model location
from properties.api.serializers import PropertySerializer  # Adjust based on your serializer location

class PropertyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
