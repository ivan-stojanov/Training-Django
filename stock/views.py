from django.shortcuts import get_object_or_404, render

from . import models

# Create your views here.
def inventory_list(request):
    inventories = models.Inventory.objects.filter(
         is_available=True
    )
    return render(request, 'stock/inventory_list.html', {
        'inventories': inventories
    })
    
    
def inventory_details(request, pk):
    inventory = get_object_or_404(
         models.Inventory,
         pk=pk,
         is_available=True
    )
    return render(request, 'stock/inventory_details.html', {
        'inventory': inventory
    })
    
    
def inventory_edit(request, pk):
    inventory = get_object_or_404(
         models.Inventory,
         pk=pk,
         is_available=True
    )
    return render(request, 'stock/inventory_edit.html', {
        'inventory': inventory
    })
    

def inventory_create(request):
    return render(request, 'stock/inventory_create.html')    


def dashboard(request):
    return render(request, 'stock/dashboard.html')


