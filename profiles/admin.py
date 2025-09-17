from django.contrib import admin
from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'phone', 'city', 'state', 'pincode', 'is_default']
    list_filter = ['is_default', 'city', 'state']
