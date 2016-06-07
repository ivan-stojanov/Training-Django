from django.shortcuts import get_object_or_404, render, render_to_response
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.db.models import Q, Sum, Count
import logging

from . import forms
from . import models

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)

# Create your views here.
def inventory_list(request): 
    inventories = models.Inventory.objects.filter(
         is_available=True
    )
    return render(request, 'stock/inventory_list.html', {
        'inventories': inventories
    })
    
    
def inventory_details(request, pk):
    #inventory = get_object_or_404(
    #     models.Inventory,
    #     pk=pk
    #)
    try:
        inventory = models.Inventory.objects.select_related(
            'itemType', 'color'                                           
        ).get(
             pk=pk
        )
    except models.Inventory.DoesNotExist:
        raise Http404
    else:
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
    #inventory = get_object_or_404(
    #     models.Inventory,
    #     pk=pk
    #)
    try:
        inventory = models.Inventory.objects.select_related(
            'itemType', 'color'                                           
        ).get(
             pk=pk
        )
    except models.Inventory.DoesNotExist:
        raise Http404
    else:
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


def inventory_search(request):
    if request.method == 'POST':
        search_text = request.POST['search_term']
        search_criteria = request.POST['search_type']
    else:
        search_text = ''
        search_criteria = ''

    sort = {}
    sort['name'] = "sort-asc"
    sort['serial_number'] = "sort-asc"
    sort['price'] = "sort-asc"
    sort['weight'] = "sort-asc"
    sort['color'] = "sort-asc"
    sort['itemType'] = "sort-asc"        
        
    if search_criteria == "ItemName":
        inventories = models.Inventory.objects.filter(
             name__icontains=search_text,
             is_available=True
        )
    elif search_criteria == "SerialNumber":
        inventories = models.Inventory.objects.filter(
             serial_number__icontains=search_text,
             is_available=True
        )     
    elif search_criteria == "Price":
        inventories = models.Inventory.objects.filter(
             price__icontains=search_text,
             is_available=True
        ) 
    elif search_criteria == "Weight":
        inventories = models.Inventory.objects.filter(
             weight__icontains=search_text,
             is_available=True
        )
    elif search_criteria == "Color":
        inventories = models.Inventory.objects.filter(
            color__color_name__icontains=search_text,
            is_available=True
        )      
    elif search_criteria == "ItemType":
        inventories = models.Inventory.objects.filter(
            itemType__type_name__icontains=search_text,
            is_available=True
        )       
    else:  
        inventories = models.Inventory.objects.filter(
             Q(name__icontains=search_text)|Q(serial_number__icontains=search_text)|
             Q(price__icontains=search_text)|Q(weight__icontains=search_text)|
             Q(color__color_name__icontains=search_text)|Q(itemType__type_name__icontains=search_text),
             is_available=True
        )
        
    if request.POST['sort_by_item'] and request.POST['sort_by_item'] == "name":
        if request.POST['sort_by_dir'] and request.POST['sort_by_dir'] == "ASC":
            sort['name'] = "sort-desc"
            inventories = inventories.order_by("name")
        elif request.POST['sort_by_dir'] and request.POST['sort_by_dir'] == "DESC":
            sort['name'] = "sort-asc"
            inventories = inventories.order_by("-name")
    elif request.POST['sort_by_item'] and request.POST['sort_by_item'] == "serial_number":
        if request.POST['sort_by_dir'] and request.POST['sort_by_dir'] == "ASC":
            sort['serial_number'] = "sort-desc"
            inventories = inventories.order_by("serial_number")
        elif request.POST['sort_by_dir'] and request.POST['sort_by_dir'] == "DESC":
            sort['serial_number'] = "sort-asc"
            inventories = inventories.order_by("-serial_number")
    elif request.POST['sort_by_item'] and request.POST['sort_by_item'] == "price":
        if request.POST['sort_by_dir'] and request.POST['sort_by_dir'] == "ASC":
            sort['price'] = "sort-desc"
            inventories = inventories.order_by("price")
        elif request.POST['sort_by_dir'] and request.POST['sort_by_dir'] == "DESC":
            sort['price'] = "sort-asc"
            inventories = inventories.order_by("-price")
    elif request.POST['sort_by_item'] and request.POST['sort_by_item'] == "weight":
        if request.POST['sort_by_dir'] and request.POST['sort_by_dir'] == "ASC":
            sort['weight'] = "sort-desc"
            inventories = inventories.order_by("weight")
        elif request.POST['sort_by_dir'] and request.POST['sort_by_dir'] == "DESC":
            sort['weight'] = "sort-asc"
            inventories = inventories.order_by("-weight")
    elif request.POST['sort_by_item'] and request.POST['sort_by_item'] == "color":
        if request.POST['sort_by_dir'] and request.POST['sort_by_dir'] == "ASC":
            sort['color'] = "sort-desc"
            inventories = inventories.order_by("color__color_name")
        elif request.POST['sort_by_dir'] and request.POST['sort_by_dir'] == "DESC":
            sort['color'] = "sort-asc"
            inventories = inventories.order_by("-color__color_name")
    elif request.POST['sort_by_item'] and request.POST['sort_by_item'] == "itemType":
        if request.POST['sort_by_dir'] and request.POST['sort_by_dir'] == "ASC":
            sort['itemType'] = "sort-desc"
            inventories = inventories.order_by("itemType__type_name")
        elif request.POST['sort_by_dir'] and request.POST['sort_by_dir'] == "DESC":
            sort['itemType'] = "sort-asc"
            inventories = inventories.order_by("-itemType__type_name")  
        
    return render_to_response('stock/ajax_search.html',{
        'inventories': inventories,
        'sort': sort
    })


def dashboard(request):
    inventories = models.Inventory.objects.filter(
         is_available=True
    )
    statistics = {}
    statistics['total_items'] = inventories.count()
    total_price = inventories.aggregate(total=Sum('price'))
    statistics['average_price'] = round(total_price['total'] / float(statistics['total_items']), 2)
    statistics['count_by_type'] = inventories.values('itemType__type_name').annotate(count=Count('itemType__type_name')).order_by('itemType__type_name')
    
    return render(request, 'stock/dashboard.html',{
        'statistics': statistics
    })


