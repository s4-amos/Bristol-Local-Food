"""
URLs for the customers app – currently only registration.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.customer_register, name='customer_register'),
]