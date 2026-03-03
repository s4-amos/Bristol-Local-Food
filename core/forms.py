from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


# Only Producer and Customer can self-register. Admin is created via createsuperuser only.
_REGISTER_ROLE_CHOICES = [
    (Profile.Role.PRODUCER, 'Producer'),
    (Profile.Role.CUSTOMER, 'Customer'),
]


class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=_REGISTER_ROLE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Django 5.0+ added usable_password radio field — remove it,
        # all registered users should always have password authentication.
        self.fields.pop('usable_password', None)
