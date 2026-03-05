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


class Product(models.Model):

    UNIT_CHOICES = [
        ("kg", "Kilogram"),
        ("g", "Gram"),
        ("litre", "Litre"),
        ("bunch", "Bunch"),
        ("each", "Each"),
        ("dozen", "Dozen"),
    ]

    CATEGORY_CHOICES = [
        ("vegetables", "Vegetables"),
        ("dairy_eggs", "Dairy & Eggs"),
        ("bakery", "Bakery"),
        ("meat", "Meat"),
        ("fruit", "Fruit"),
        ("honey_preserves", "Honey & Preserves"),
        ("drinks", "Drinks"),
        ("other", "Other"),
    ]

    AVAILABILITY_CHOICES = [
        ("in_season", "In Season (Available)"),
        ("out_of_season", "Out of Season (Unavailable)"),
        ("limited", "Limited Stock"),
    ]

    producer = models.ForeignKey(
        ProducerProfile,
        on_delete=models.CASCADE,
        related_name="products"
    )
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="other")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    stock_quantity = models.PositiveIntegerField(default=0)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default="in_season")
    harvest_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    def __str__(self):
        return self.name