from django.urls import path

from .views import *

urlpatterns = [

    path(
        '',
        sales_list,
        name='sales_list'
    ),

    path(
        'add/',
        add_sale,
        name='add_sale'
    ),

]