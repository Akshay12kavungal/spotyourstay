# properties/api/urls.py

from django.urls import path
from .views import PropertyListCreateAPIView, PropertyDetailAPIView  # Make sure this path is correct

urlpatterns = [
    path('properties/', PropertyListCreateAPIView.as_view(), name='property-list-create'),
    path('properties/<int:pk>/', PropertyDetailAPIView.as_view(), name='property-detail'),
]
