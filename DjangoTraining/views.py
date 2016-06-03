from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("home page of the project")
    return render(request, 'home.html')