from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def home_page(request):
    return HttpResponseRedirect(reverse('stock:dashboard'))
    #return render(request, 'home.html')
