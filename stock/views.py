from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inventory_list(request):
    return HttpResponse("home page of the app")