from django.urls import path

from .views import *

urlpatterns = [

    path(
        '',
        inventory_list,
        name='inventory_list'
    ),

    path(
        'add/',
        add_inventory,
        name='add_inventory'
    ),

]