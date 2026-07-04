from django.shortcuts import render, redirect

from .models import Inventory

from .forms import InventoryForm

from products.models import Product

from django.contrib.auth.decorators import login_required

@login_required
def inventory_list(request):

    inventory_records = Inventory.objects.all().order_by('-date')

    return render(
        request,
        'inventory/inventory_list.html',
        {
            'inventory_records': inventory_records
        }
    )

@login_required
def add_inventory(request):

    if request.method == 'POST':

        form = InventoryForm(request.POST)

        if form.is_valid():

            inventory = form.save(commit=False)

            product = inventory.product

            if inventory.transaction_type == 'IN':

                product.stock += inventory.quantity

            elif inventory.transaction_type == 'OUT':

                product.stock -= inventory.quantity

            elif inventory.transaction_type == 'ADJUSTMENT':

                product.stock = inventory.quantity

            product.save()

            inventory.save()

            return redirect('inventory_list')

    else:

        form = InventoryForm()

    return render(
        request,
        'inventory/add_inventory.html',
        {
            'form': form
        }
    )