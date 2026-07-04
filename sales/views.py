from django.shortcuts import render
from django.shortcuts import redirect

from .models import Sale
from .forms import SaleForm

from products.models import Product

from django.contrib.auth.decorators import login_required

@login_required
def sales_list(request):

    sales = Sale.objects.all().order_by('-sale_date')

    return render(
        request,
        'sales/sales_list.html',
        {
            'sales': sales
        }
    )

@login_required
def add_sale(request):

    if request.method == 'POST':

        form = SaleForm(request.POST)

        if form.is_valid():

            sale = form.save(commit=False)

            product = sale.product

            quantity = sale.quantity

            if product.stock >= quantity:

                product.stock -= quantity

                product.save()

                sale.amount = (
                    quantity * product.price
                )

                sale.save()

                return redirect('sales_list')

            else:

                return render(
                    request,
                    'sales/error.html',
                    {
                        'message':
                        'Not enough stock available'
                    }
                )

    else:

        form = SaleForm()

    return render(
        request,
        'sales/add_sale.html',
        {
            'form': form
        }
    )