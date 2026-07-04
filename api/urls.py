from django.urls import path
from .views import *

urlpatterns = [

    path(
        "products/",
        product_list_api,
        name="product_list_api"
    ),

    path(
        "products/<int:pk>/",
        product_detail_api,
        name="product_detail_api"
    ),

    path(
        "products/create/",
        product_create_api,
        name="product_create_api"
    ),

    path(
        "products/update/<int:pk>/",
        product_update_api,
        name="product_update_api"
    ),

    path(
        "products/delete/<int:pk>/",
        product_delete_api,
        name="product_delete_api"
    ),

    # Inventory APIs

    path(
        "inventory/",
        inventory_list_api,
        name="inventory_list_api"
    ),

    path(
        "inventory/<int:pk>/",
        inventory_detail_api,
        name="inventory_detail_api"
    ),

    path(
        "inventory/create/",
        inventory_create_api,
        name="inventory_create_api"
    ),

    path(
        "inventory/update/<int:pk>/",
        inventory_update_api,
        name="inventory_update_api"
    ),

    path(
        "inventory/delete/<int:pk>/",
        inventory_delete_api,
        name="inventory_delete_api"
    ),
    # Sales APIs

    path(
        "sales/",
        sales_list_api,
        name="sales_list_api"
    ),

    path(
        "sales/<int:pk>/",
        sales_detail_api,
        name="sales_detail_api"
    ),

    path(
        "sales/create/",
        sales_create_api,
        name="sales_create_api"
    ),

    path(
        "sales/update/<int:pk>/",
        sales_update_api,
        name="sales_update_api"
    ),

    path(
        "sales/delete/<int:pk>/",
        sales_delete_api,
        name="sales_delete_api"
    ),
        path(
    "dashboard/",
    dashboard_api,
    name="dashboard_api"
    ),

    path(
        "analytics/",
        ai_api,
        name="ai_api"
    ),

    path(
        "",
        api_home,
        name="api_home"
    ),
]

