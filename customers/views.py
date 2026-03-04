"""
View for customer registration.
Handles form submission, duplicate email check, and profile creation.
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import User
from .models import CustomerProfile

def customer_register(request):
    if request.method == 'POST':
        # Extract form data
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST.get('address', '')
        postcode = request.POST.get('postcode', '')
        phone = request.POST.get('phone', '')
        delivery_address = request.POST.get('default_delivery_address', '')

        # Check for existing email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please log in.')
            return render(request, 'customers/register.html')

        # If delivery address not provided, use user's address
        if not delivery_address:
            delivery_address = address

        # Create user (username = email)
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role='customer',           # default role
            address=address,
            postcode=postcode
        )
        # Create associated customer profile
        CustomerProfile.objects.create(
            user=user,
            default_delivery_address=delivery_address,
            phone=phone
        )
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('login')

    # GET request – show empty form
    return render(request, 'customers/register.html')