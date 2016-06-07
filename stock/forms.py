from django import forms
from django.contrib.auth.models import User

from . import models


class InventoryForm(forms.ModelForm):
    class Meta:
        model = models.Inventory
        fields = [
            'name',
            'serial_number',
            'description',
            'price',
            'weight',
            'photo',
            'is_available',
            'itemType',
            'color',
        ]
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password'
        ]