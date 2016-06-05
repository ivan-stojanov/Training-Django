from django.shortcuts import render

from . import models

# Create your views here.
def inventory_list(request):
    inventories = models.Inventory.objects.filter(
         is_available=True
    )
    return render(request, 'stock/inventory_list.html', {
        'inventories': inventories
    })


def dashboard(request):
    return render(request, 'stock/dashboard.html')


