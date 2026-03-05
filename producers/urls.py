from django.urls import path
from . import views

app_name = "producers"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.product_add, name="product_add"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),
]