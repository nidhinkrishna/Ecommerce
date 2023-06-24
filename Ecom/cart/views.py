from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from store.models import Products
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

def _cart_id(request):
    cart = request.session.session_key

    if not cart:
        cart = request.session.create()
    return cart



def add_cart(request,product_id):
    current_user = request.user
    product = Products.objects.get(id=product_id)
   
        
    if current_user.is_authenticated:
        is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product, user=current_user)
            for item in cart_item:
                
                item.quantity += 1
                item.save()


        else:
            cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            user = current_user,

        )
            cart_item.save()
        return redirect('cart')   
    else:
        
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id = _cart_id(request)
            )
        cart.save()     
        # cart = Cart.objects.get(cart_id=_cart_id(request))
        # cart.save()
        is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product, cart=cart)
        else:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart,
            )
            cart_item.save()
        return redirect('cart')


    
    # current_url = request.META.get('HTTP_REFERER')
    
    
    # return redirect(current_url)

def cart(request,total=0,quantity=0,cart_item=None,delivery_fee = 0,
        grand_total = 0):
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.filter(user = request.user)

        else:
            cart = Cart.objects.get(cart_id = _cart_id(request))
            cart_item = CartItem.objects.filter(cart=cart)


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

def decrement_cart(request,product_id,cart_item_id):
  
    product = get_object_or_404(Products,id = product_id)
    try:
        if request.user.is_authenticated:
           
            cart_item = CartItem.objects.get(product=product,user=request.user,id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id = _cart_id(request))
            cart_item = CartItem.objects.get(product=product,cart=cart,id=cart_item_id)
   
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')


def remove_item(request,product_id,cart_item_id):
   
    product = get_object_or_404(Products,id = product_id)
    if request.user.is_authenticated:
       
        cart_item = CartItem.objects.get(product=product,user=request.user,id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_item = CartItem.objects.get(cart=cart,product=product,id=cart_item_id)

    cart_item.delete()
    return redirect('cart')


 

@login_required(login_url='login')
def checkout(request,total=0,quantity=0,cart_item=None,delivery_fee = 0,
        grand_total = 0):
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id = _cart_id(request))
            cart_item = CartItem.objects.filter(cart=cart)


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



    return render(request,'cart/checkout.html',context)