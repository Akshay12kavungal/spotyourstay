# properties/urls.py

from django.urls import include, path
from .api.urls import urlpatterns as api_urlpatterns  # Make sure the import path is correct

urlpatterns = [
    path('api/', include(api_urlpatterns)),  # Include API URLs under a specific path
]
