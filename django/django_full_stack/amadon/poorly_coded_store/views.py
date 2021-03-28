from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


# NEED TO MAKE CHECKOUT BE LAST ORDER INFO
# AS WELL AS CONTEXT PASSING "RENDERING"

def checkout(request): #POST
    last_order = Order.objects.last()
    price = last_order.total_price
    total_quantity = Order.objects.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum']
    total_price = Order.objects.aggregate(Sum('total_price'))['total_price__sum']
    context = {
        'total_quantity': total_quantity,
        'total_price': total_price,
        'this_price': price,
    }
    return render(request, "store/checkout.html", context)


# MAKE PURCHASE CHECK TO SEE IF THE CURRENT PRODUCT ID
# IS THIS PRODUCT ID (IF NOT, REDIRECT('/')), IF SO, 
# CALCULATE QUANITY AND TOTAL_CHARGE, CREATE,
# AND REDIRECT TO CHECKOUT

def purchase(request):
    if request.method == 'POST':
        this_product = Product.objects.filter(id=request.POST['id']) # LIST of all products that match this ID
        if not this_product:
            redirect('/')
        else:
            quantity = int(request.POST['quantity'])
            total_charge = quantity * (float(this_product[0].price))
            Order.objects.create(quantity_ordered=quantity, total_price=total_charge)
            return redirect('/checkout')
    else:
        redirect('/')

