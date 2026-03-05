"""
Main URL configuration. Includes admin and app URLs.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),                     # Django admin
    path('', include('core.urls')),                      # Core app (home, login, logout)
    path('customers/', include('customers.urls')),       # Customer app (registration)
    path("producers/", include("producers.urls")),
]