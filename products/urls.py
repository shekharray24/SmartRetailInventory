from django.urls import path

from .views import *

urlpatterns = [

    path('', dashboard, name='dashboard'),

    path(
        'products/',
        product_list,
        name='product_list'
    ),

    path(
        'products/add/',
        add_product,
        name='add_product'
    ),

    path(
        'products/edit/<int:pk>/',
        edit_product,
        name='edit_product'
    ),

    path(
        'products/delete/<int:pk>/',
        delete_product,
        name='delete_product'
    ),
]