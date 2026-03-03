from django.contrib import admin

from .models import Category, Product, ProducerProfile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProducerProfile)
class ProducerProfileAdmin(admin.ModelAdmin):
    list_display = ['farm_name', 'user', 'phone', 'farm_postcode']
    search_fields = ['farm_name', 'user__username', 'farm_postcode']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'producer', 'category', 'price', 'unit', 'stock_quantity']
    list_filter = ['category', 'unit']
    search_fields = ['name', 'producer__farm_name']
