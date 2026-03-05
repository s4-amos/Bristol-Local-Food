"""
URL patterns for the core app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                     # Home page
    path('login/', views.LoginView.as_view(), name='login'), # Login
    path('logout/', views.LogoutView.as_view(), name='logout'), # Logout
]