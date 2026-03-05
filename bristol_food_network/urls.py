"""
Main URL configuration. Includes admin and app URLs.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),                     # Django admin
    path('', include('core.urls')),                      # Core app (home, login, logout)
    path('customers/', include('customers.urls')),       # Customer app (registration)
    path("producers/", include("producers.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)