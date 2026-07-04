from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from .serializers import ProductSerializer

from inventory.models import Inventory
from sales.models import Sale

from .serializers import ( ProductSerializer, InventorySerializer, SaleSerializer )

from django.db.models import Sum, F
from ai_engine.database_detector import detect_sales_anomalies


@api_view(["GET"])
def product_list_api(request):

    products = Product.objects.all()

    serializer = ProductSerializer(
        products,
        many=True
    )

    return Response(serializer.data)

from django.shortcuts import get_object_or_404


@api_view(["GET"])
def product_detail_api(request, pk):

    product = get_object_or_404(Product, id=pk)

    serializer = ProductSerializer(product)

    return Response(serializer.data)


@api_view(["POST"])
def product_create_api(request):

    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

@api_view(["PUT"])
def product_update_api(request, pk):

    product = get_object_or_404(Product, id=pk)

    serializer = ProductSerializer(
        product,
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors, status=400)

@api_view(["DELETE"])
def product_delete_api(request, pk):

    product = get_object_or_404(Product, id=pk)

    product.delete()

    return Response(
        {"message": "Product deleted successfully"}
    )

# Inventory List API

@api_view(["GET"])
def inventory_list_api(request):

    inventory = Inventory.objects.all()

    serializer = InventorySerializer(
        inventory,
        many=True
    )

    return Response(serializer.data)

@api_view(["GET"])
def inventory_detail_api(request, pk):

    item = get_object_or_404(
        Inventory,
        id=pk
    )

    serializer = InventorySerializer(item)

    return Response(serializer.data)

@api_view(["POST"])
def inventory_create_api(request):

    serializer = InventorySerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(
            serializer.data,
            status=201
        )

    return Response(
        serializer.errors,
        status=400
    )

@api_view(["PUT"])
def inventory_update_api(request, pk):

    item = get_object_or_404(
        Inventory,
        id=pk
    )

    serializer = InventorySerializer(
        item,
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=400
    )

@api_view(["DELETE"])
def inventory_delete_api(request, pk):

    item = get_object_or_404(
        Inventory,
        id=pk
    )

    item.delete()

    return Response({

        "message":

        "Inventory deleted successfully"

    })

# Sales API List

@api_view(["GET"])
def sales_list_api(request):

    sales = Sale.objects.all()

    serializer = SaleSerializer(
        sales,
        many=True
    )

    return Response(serializer.data)

@api_view(["POST"])
def sales_create_api(request):

    serializer = SaleSerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(
            serializer.data,
            status=201
        )

    return Response(
        serializer.errors,
        status=400
    )

@api_view(["GET"])
def sales_detail_api(request, pk):

    sale = get_object_or_404(
        Sale,
        id=pk
    )

    serializer = SaleSerializer(sale)

    return Response(serializer.data)

@api_view(["PUT"])
def sales_update_api(request, pk):

    sale = get_object_or_404(
        Sale,
        id=pk
    )

    serializer = SaleSerializer(
        sale,
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=400
    )

@api_view(["DELETE"])
def sales_delete_api(request, pk):

    sale = get_object_or_404(
        Sale,
        id=pk
    )

    sale.delete()

    return Response({

        "message":

        "Sale deleted successfully"

    })

#Dashboard API

@api_view(["GET"])
def dashboard_api(request):

    total_products = Product.objects.count()

    total_sales = Sale.objects.count()

    total_revenue = (
        Sale.objects.aggregate(
            total=Sum("amount")
        )["total"] or 0
    )

    inventory_value = (
        Product.objects.aggregate(
            total=Sum(F("price") * F("stock"))
        )["total"] or 0
    )

    low_stock = Product.objects.filter(
        stock__lt=20
    ).count()

    anomalies = len(
        detect_sales_anomalies()
    )

    return Response({

        "total_products": total_products,

        "total_sales": total_sales,

        "total_revenue": total_revenue,

        "inventory_value": inventory_value,

        "low_stock": low_stock,

        "anomalies": anomalies

    })

#Ai API

@api_view(["GET"])
def ai_api(request):

    anomalies = detect_sales_anomalies()

    return Response({

        "total_anomalies": len(anomalies),

        "results": anomalies

    })

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_home(request):

    return Response({

        "project": "Smart Retail Inventory Management System",

        "version": "1.0",

        "developer": "Shekhar Ray",

        "available_endpoints": {

            "Products": {

                "GET All": "/api/products/",

                "POST": "/api/products/create/",

                "GET One": "/api/products/<id>/",

                "PUT": "/api/products/update/<id>/",

                "DELETE": "/api/products/delete/<id>/"

            },

            "Inventory": {

                "GET All": "/api/inventory/",

                "POST": "/api/inventory/create/",

                "GET One": "/api/inventory/<id>/",

                "PUT": "/api/inventory/update/<id>/",

                "DELETE": "/api/inventory/delete/<id>/"

            },

            "Sales": {

                "GET All": "/api/sales/",

                "POST": "/api/sales/create/",

                "GET One": "/api/sales/<id>/",

                "PUT": "/api/sales/update/<id>/",

                "DELETE": "/api/sales/delete/<id>/"

            },

            "Dashboard": "/api/dashboard/",

            "AI Analytics": "/api/analytics/"

        }

    })