from django.db import models
from django.conf import settings

class ProducerProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="producer_profile"
    )

    farm_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    phone_number = models.CharField(max_length=20)
    business_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    website = models.URLField(blank=True)

    FARM_TYPE_CHOICES = [
        ("vegetables", "Vegetables"),
        ("dairy", "Dairy"),
        ("bakery", "Bakery"),
        ("meat", "Meat"),
        ("mixed", "Mixed Produce"),
    ]

    farm_type = models.CharField(max_length=20, choices=FARM_TYPE_CHOICES)

    offers_delivery = models.BooleanField(default=False)
    offers_pickup = models.BooleanField(default=True)

    def __str__(self):
        return self.farm_name