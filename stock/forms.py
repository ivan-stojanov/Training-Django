from django import forms

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