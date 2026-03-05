from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import uuid

class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('producer', 'Producer'),
        ('admin', 'Admin'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    address = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=20, blank=True)

    # Make username optional because we log in with email
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']  # keep as-is

    def save(self, *args, **kwargs):
        if not self.username:
            base = slugify(self.email.split("@")[0]) or "user"
            self.username = f"{base}-{uuid.uuid4().hex[:6]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email