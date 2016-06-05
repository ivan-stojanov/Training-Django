from django.contrib import admin

from .models import Inventory
from .models import ItemType
from .models import Color

# Register your models here.

admin.site.register(Inventory)
admin.site.register(ItemType)
admin.site.register(Color)