from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^$', views.inventory_list,
        name='list'),
    url(r'^register/$', views.register, 
        name='register'),
    url(r'^login/$', views.login_user, 
        name='login'),
    url(r'^logout/$', views.logout_user, 
        name='logout'),
    url(r'inventory/(?P<pk>\d+)/$', views.inventory_details, 
        name='details'),
    url(r'inventory/edit/(?P<pk>\d+)/$', views.inventory_edit, 
        name='edit'),
    url(r'inventory/delete/(?P<pk>\d+)/$', views.inventory_delete, 
        name='delete'),
    url(r'inventory/create/$', views.inventory_create, 
        name='create'),
    url(r'inventory/search/$', views.inventory_search, 
        name='search'),
    url(r'dashboard/$', views.dashboard,
        name='dashboard'),
]