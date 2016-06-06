from django import forms

from . import models


class TextForm(forms.ModelForm):
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