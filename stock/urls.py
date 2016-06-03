from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^$', views.inventory_list,
        name='list'),
    url(r'dashboard/$', views.dashboard,
        name='dashboard'),
]