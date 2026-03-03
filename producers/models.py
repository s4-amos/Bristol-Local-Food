from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProducerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='producer_profile',
    )
    farm_name = models.CharField(max_length=200)
    farm_address = models.TextField()
    farm_postcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.farm_name


class Product(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('unit', 'Unit/Each'),
        ('bunch', 'Bunch'),
        ('litre', 'Litre'),
        ('dozen', 'Dozen'),
        ('box', 'Box'),
    ]

    producer = models.ForeignKey(
        'producers.ProducerProfile',
        on_delete=models.CASCADE,
        related_name='products',
    )
    category = models.ForeignKey(
        'producers.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products',
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default='unit')
    stock_quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} (£{self.price}/{self.unit})'
