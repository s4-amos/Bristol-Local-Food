"""
Custom User model extending Django's AbstractUser.
Uses email as the unique identifier instead of username.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Role choices for future use (e.g., producer, admin)
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('producer', 'Producer'),
        ('admin', 'Admin'),
    )
    email = models.EmailField(unique=True)               # Email must be unique
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    address = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=20, blank=True)

    # Use email as the login field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    def __str__(self):
        return self.email