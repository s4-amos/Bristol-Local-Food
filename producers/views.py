from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ProducerRegistrationForm, ProductForm
from .models import ProducerProfile, Product


def register(request):
    if request.method == "POST":
        form = ProducerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("producers:dashboard")   # redirect after registration
    else:
        form = ProducerRegistrationForm()

    return render(request, "producers/register.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "producers/dashboard.html")


@login_required
def product_list(request):
    try:
        profile = request.user.producer_profile
    except ProducerProfile.DoesNotExist:
        return redirect("producers:register")
    products = profile.products.all()
    return render(request, "producers/product_list.html", {"products": products})


@login_required
def product_add(request):
    try:
        profile = request.user.producer_profile
    except ProducerProfile.DoesNotExist:
        return redirect("producers:register")
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.producer = profile
            product.save()
            return redirect("producers:product_list")
    else:
        form = ProductForm()
    return render(request, "producers/product_form.html", {"form": form})


@login_required
def product_delete(request, pk):
    try:
        profile = request.user.producer_profile
    except ProducerProfile.DoesNotExist:
        return redirect("producers:register")
    product = get_object_or_404(Product, pk=pk, producer=profile)
    if request.method == "POST":
        product.delete()
    return redirect("producers:product_list")