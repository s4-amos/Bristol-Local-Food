"""
Views for the core app:
- home: placeholder home page
- LoginView: custom login view
- LogoutView: custom logout view accepting GET
"""
from django.contrib.auth import views as auth_views, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

def home(request):
    """Render the home page (placeholder)."""
    return render(request, 'core/home.html')

class LoginView(auth_views.LoginView):
    """Custom login view that uses our template and redirects authenticated users."""
    template_name = 'core/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')   # After login, go to home

class LogoutView(View):
    """Custom logout view that accepts GET requests (simpler for navbar links)."""
    def get(self, request):
        logout(request)
        return redirect('login')