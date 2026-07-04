# from multiprocessing import context
# from urllib import request

from django.db.models.functions import TruncMonth
from django.db.models.functions import TruncDate
from django.db.models import Count
import json


from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F

from .models import Product
from .forms import ProductForm

from sales.models import Sale
from inventory.models import Inventory

from ai_engine.database_detector import detect_sales_anomalies

def dashboard(request):

    total_products = Product.objects.count()

    total_sales = Sale.objects.count()

    total_revenue = (
        Sale.objects.aggregate(
            total=Sum('amount')
        )['total'] or 0
    )

    inventory_value = (
        Product.objects.aggregate(
            total=Sum(F('price') * F('stock'))
        )['total'] or 0
    )

    low_stock = Product.objects.filter(
        stock__lt=20
    ).count()

    recent_sales = Sale.objects.order_by('-sale_date')[:5]

    recent_inventory = Inventory.objects.order_by('-date')[:5]

    low_stock_products = Product.objects.filter(
    stock__lt=20
    ).order_by('stock')

    sales_anomalies = detect_sales_anomalies()

    daily_sales = (
    Sale.objects
    .annotate(day=TruncDate("sale_date"))
    .values("day")
    .annotate(total=Sum("amount"))
    .order_by("day")
)

    chart_labels = [
        str(item["day"])
        for item in daily_sales 
    ]

    chart_data = [
        item["total"]
        for item in daily_sales
    ]

    monthly_sales = (
    Sale.objects
    .annotate(month=TruncMonth("sale_date"))
    .values("month")
    .annotate(total=Sum("id"))
    .order_by("month")
)

    monthly_labels = [
        item["month"].strftime("%b %Y")
        for item in monthly_sales
    ]

    monthly_data = [
        item["total"]
        for item in monthly_sales
    ]

    category_data = (
        Product.objects
        .values("category")
        .annotate(total=Count("id"))
        .order_by("category")
    )

    category_labels = [
        item["category"]
        for item in category_data
    ]

    category_values = [
        item["total"]
        for item in category_data
    ]

    context = {

    "total_products": total_products,

    "total_sales": total_sales,

    "total_revenue": total_revenue,

    "inventory_value": inventory_value,

    "low_stock": low_stock,

    "anomalies": len(sales_anomalies),

    "recent_sales": recent_sales,

    "recent_inventory": recent_inventory,

    "low_stock_products": low_stock_products,

    "sales_anomalies": sales_anomalies,

    "chart_labels": json.dumps(chart_labels),

    "chart_data": json.dumps(chart_data),

    "monthly_labels": json.dumps(monthly_labels),

    "monthly_data": json.dumps(monthly_data),

    "category_labels": json.dumps(category_labels),

    "category_values": json.dumps(category_values),


}

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )


def product_list(request):

    products = Product.objects.all()

    search = request.GET.get("search")

    category = request.GET.get("category")

    brand = request.GET.get("brand")

    if search:

        products = products.filter(name__icontains=search)

    if category:

        products = products.filter(category=category)

    if brand:

        products = products.filter(brand=brand)

    categories = (
        Product.objects
        .values_list("category", flat=True)
        .distinct()
    )

    brands = (
        Product.objects
        .values_list("brand", flat=True)
        .distinct()
    )

    context = {

        "products": products,

        "categories": categories,

        "brands": brands,

        "selected_category": category,

        "selected_brand": brand,

        "search": search,

    }

    return render(
        request,
        "products/product_list.html",
        context
    )

def add_product(request):

    if request.method == 'POST':

        form = ProductForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('product_list')

    else:

        form = ProductForm()

    return render(
        request,
        'products/add_product.html',
        {'form': form}
    )


def edit_product(request, pk):

    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            instance=product
        )

        if form.is_valid():

            form.save()

            return redirect('product_list')

    else:

        form = ProductForm(instance=product)

    return render(
        request,
        'products/edit_product.html',
        {'form': form}
    )


def delete_product(request, pk):

    product = get_object_or_404(Product, id=pk)

    product.delete()

    return redirect('product_list')