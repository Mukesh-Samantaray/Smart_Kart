from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'phone', 'street', 'city', 'state', 'pincode', 'country', 'is_default']
