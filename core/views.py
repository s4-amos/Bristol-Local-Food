from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from .forms import RegisterForm


def home(request):
    return render(request, 'core/home.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']
            user.profile.role = role
            user.profile.save()
            login(request, user)
            if role == 'PRODUCER':
                return redirect('producers:producer_register')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'core/login.html'


class CustomLogoutView(LogoutView):
    # POST-only logout (recommended)
    pass


def role_required(*allowed_roles):
    def decorator(view_func):
        @login_required
        def _wrapped(request, *args, **kwargs):
            if request.user.profile.role not in allowed_roles:
                return HttpResponseForbidden('Forbidden: insufficient role')
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
