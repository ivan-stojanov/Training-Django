from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inventory_list(request):
    return render(request, 'stock/inventory_list.html')
    return HttpResponse("home page of the inventory_list")

def dashboard(request):
    return render(request, 'stock/dashboard.html')
    return HttpResponse("home page of the dashboard")


