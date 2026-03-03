from django import forms

from .models import ProducerProfile, Product


class ProducerProfileForm(forms.ModelForm):
    class Meta:
        model = ProducerProfile
        fields = ['farm_name', 'farm_address', 'farm_postcode', 'phone', 'description']
        widgets = {
            'farm_address': forms.Textarea(attrs={'rows': 3}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'unit', 'stock_quantity']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
