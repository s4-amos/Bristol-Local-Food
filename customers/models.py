"""
CustomerProfile model – extends the User with additional fields.
One‑to‑one relationship with User.
"""
from django.db import models
from core.models import User

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                 related_name='customer_profile')
    default_delivery_address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Customer: {self.user.email}"