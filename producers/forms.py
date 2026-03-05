from django import forms
from django.contrib.auth import get_user_model
from .models import ProducerProfile

User = get_user_model()

class ProducerRegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    farm_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=20)
    business_address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "address", "postcode"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = "producer"
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

            ProducerProfile.objects.create(
                user=user,
                farm_name=self.cleaned_data["farm_name"],
                phone_number=self.cleaned_data["phone_number"],
                business_address=self.cleaned_data["business_address"],
                city=self.cleaned_data["city"],
            )

        return user