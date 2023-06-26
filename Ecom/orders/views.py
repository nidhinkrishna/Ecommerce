from django.shortcuts import render,HttpResponse,redirect
from cart.models import CartItem
from .forms import OrderForm
from .models import *
import datetime
from django.contrib import messages

# Create your views here.

def payments(request):
    return render(request,'orders/payments.html')
def place_order(request):
    current_user = request.user

    grand_total =0
    delivery_fee = 0
    total = 0
    # cart_items = None

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user = current_user)
        for cart_item in cart_items:
            total += (cart_item.product.selling_price * cart_item.quantity)
            cart_count = cart_items.count()
        if cart_count <= 0:
            return redirect('store')
        
        
    
    if total > 20000 or total == 0:
        delivery_fee = 0
        grand_total = total
    
    else:
        delivery_fee = 49
        grand_total = total + delivery_fee

    
    
    if request.method == "POST":
         
        form = OrderForm(request.POST)
        if form.is_valid():
            # Store all the billing information inside Order table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.mobile_no = form.cleaned_data['mobile_no']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
          
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.delivery_fee = delivery_fee
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d") 
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
          

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order': order,
                'cart_item': cart_items,
                'total': total,
                'deliver_fee': delivery_fee,
                'grand_total': grand_total,
            }

            return render(request,'orders/payments.html',context)
    else:
        messages.error(request,'some error occured')
        return redirect('checkout')


    
    




