from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ProducerRegistrationForm


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