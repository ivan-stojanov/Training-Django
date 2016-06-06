from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from . import forms
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
         pk=pk
    )
    return render(request, 'stock/inventory_details.html', {
        'inventory': inventory
    })
    

def inventory_create(request):
    form = forms.InventoryForm()
    
    if request.method == 'POST':
        form = forms.InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            inventory = form.save(commit=False)
            '''perform additional custom actions, if needed'''
            inventory.save()
            messages.add_message(
                                 request,
                                 messages.SUCCESS,
                                 "Inventory Created: {}!".format(form.cleaned_data['name'])
                                 )
            return HttpResponseRedirect(inventory.get_absolute_url())    
    
    return render(request, 'stock/inventory_form.html', {
        'form': form
    })       
    
    
def inventory_edit(request, pk):
    inventory = get_object_or_404(
         models.Inventory,
         pk=pk
    )
    form = forms.InventoryForm(instance=inventory)
    
    if request.method == 'POST':
        form = forms.InventoryForm(instance=inventory, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 
                             "Inventory Updated: {}!".format(form.cleaned_data['name']))
            return HttpResponseRedirect(inventory.get_absolute_url())  
    
    return render(request, 'stock/inventory_form.html', {
        'form': form
    })
    
    
def inventory_delete(request, pk):
    inventory = get_object_or_404(
         models.Inventory,
         pk=pk
    )    
    messages.success(request, 
                     "Inventory Deleted: {}!".format(inventory.name))
    inventory.delete();
    return HttpResponseRedirect(reverse('stock:list')) 


def dashboard(request):
    return render(request, 'stock/dashboard.html')


