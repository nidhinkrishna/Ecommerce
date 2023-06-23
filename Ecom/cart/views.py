from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from store.models import Products
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages



# Create your views here.

def _cart_id(request):
    cart = request.session.session_key

    if not cart:
        cart = request.session.create()
    return cart



def add_cart(request,product_id):
    product = Products.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart.save()
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try:

        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity+=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
        messages.success(request,'Item Added to Cart')
    
    current_url = request.META.get('HTTP_REFERER')
    
    
    return redirect(current_url)

def cart(request,total=0,quantity=0,cart_item=None,delivery_fee = 0,
        grand_total = 0):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_item = CartItem.objects.filter(cart=cart,is_active = True)


        for cart_it in cart_item:
            total += (cart_it.product.selling_price * cart_it.quantity)
            quantity += cart_it.quantity

        
        if total > 20000 or total == 0:
            delivery_fee = 0
            grand_total = total
        
        else:
            delivery_fee = 49
            grand_total = total + delivery_fee

    except ObjectDoesNotExist:
        pass 

    context = {
        'total':total,
        'quantity':quantity,
        'cart_item':cart_item,
        'delivery_fee':delivery_fee,
        'grand_total':grand_total
    }

    return render(request,'cart/cart.html',context)

def decrement_cart(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Products,id = product_id)
    cart_item = CartItem.objects.get(cart=cart,product=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_item(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Products,id = product_id)
    cart_item = CartItem.objects.get(cart=cart,product=product)

    cart_item.delete()
    return redirect('cart')


 


def checkout(request):
    


    return render(request,'cart/checkout.html')