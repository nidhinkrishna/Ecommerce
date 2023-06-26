from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from cart.models import CartItem
from .forms import OrderForm
from .models import *
import datetime
from store.models import Products
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import json

# Create your views here.

def payments(request):
    
    body = json.loads(request.body)
    order = Order.objects.get(user=request.user, is_ordered=False, order_number=body['orderID'])

    # Store transaction details inside Payment model
    payment = Payment(
        user = request.user,
        payment_id = body['transID'],
        payment_method = body['payment_method'],
        amount_paid = order.order_total,
        status = body['status'],
    )
    payment.save()

    order.payment = payment
    order.is_ordered = True
    order.save()

    # Move the cart items to Order Product table
    cart_items = CartItem.objects.filter(user=request.user)

    for item in cart_items:
        orderproduct = OrderProduct()
        orderproduct.order_id = order.id
        orderproduct.payment = payment
        orderproduct.user_id = request.user.id
        orderproduct.product_id = item.product_id
        orderproduct.quantity = item.quantity
        orderproduct.product_price = item.product.selling_price
        orderproduct.ordered = True
        orderproduct.save()

      


        # Reduce the quantity of the sold products
        product = Products.objects.get(id=item.product_id)
        product.stock -= item.quantity
        product.save()

    # Clear cart
    CartItem.objects.filter(user=request.user).delete()

    # Send order recieved email to customer
    mail_subject = 'Thank you for your order!'
    message = render_to_string('orders/order_recieved_email.html', {
        'user': request.user,
        'order': order,
    })
    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()

    # Send order number and transaction id back to sendData method via JsonResponse
    data = {
        'order_number': order.order_number,
        'transID': payment.payment_id,
    }
    return JsonResponse(data)

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
                'delivery_fee': delivery_fee,
                'grand_total': grand_total,
            }

            return render(request,'orders/payments.html',context)
    else:
        messages.error(request,'some error occured')
        return redirect('checkout')


    
    




def order_complete(request):

    return render(request,'orders/order_complete.html')