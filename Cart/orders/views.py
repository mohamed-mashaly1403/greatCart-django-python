import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.backends import django
import django.core.mail

from .form import OrderForm
from busket.models import busketItems
from .models import Order, Payment, orderPoduct
from store.models import product
import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string




def place_order(request,total=0,quantity=0):
    # Gtotal = 0
    # tax = 0
    current_user = request.user
    cart_items = busketItems.objects.filter(user=current_user)
    cart_count =cart_items.count()
    if cart_count <= 0:
        return redirect('store')
    if request.method == 'POST':
        form = OrderForm(request.POST)

        for cart_item in cart_items:
            quantity += cart_item.quantity
            total += cart_item.product_busket_item.product_price * cart_item.quantity
        tax = (0.02 * total)
        Gtotal = total + tax
        print(form.errors)
        if form.is_valid():
            print(form.errors)
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.user = current_user
            data.total = Gtotal
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime('%Y%d%m')
            order_number = current_date+str(data.id)
            data.order_number = order_number
            data.save()
            order = Order.objects.get(user=current_user,is_ordered=False,order_number=order_number)
            context ={
                'order':order,
                'cart_items':cart_items,
                'total':total,
                'tax':tax,
                'Gtotal':Gtotal

            }
            return render(request,'orders/payments.html',context)
        else:
            print('not vaild')
            print(form.errors)
            return redirect('checkout')
def payments(request):
    current_user = request.user
    body = json.loads(request.body)
    print(body)
    order = Order.objects.get(user= current_user,is_ordered=False, order_number=body['orderID'])
    payment = Payment(
        user = current_user,
        payment_id = body['transID'],
        payment_method = body['payment_method'],
        status = body['status'],
        amount_paid= order.total,

    )
    payment.save()
    order.payment = payment
    order.is_ordered = True
    order.save()
    cart_items = busketItems.objects.filter(user=current_user)
    for item in cart_items:
        #fill order product model
        orderPoductt = orderPoduct()
        orderPoductt.order_id = order.id
        orderPoductt.payment = payment
        orderPoductt.user_id = current_user.id
        orderPoductt.product_id = item.product_busket_item_id
        orderPoductt.quantity = item.quantity
        orderPoductt.product_price = item.product_busket_item.product_price
        orderPoductt.ordered = True
        orderPoductt.save()
        # bring variations because it is many to many
        cart_item = busketItems.objects.get(id=item.id)
        product_variation= cart_item.variations.all()
        orderPoducttt = orderPoduct.objects.get(id=orderPoductt.id)
        orderPoducttt.variations.set(product_variation)
        orderPoducttt.save()
        # Reduce the quantity
        productt = product.objects.get(id=item.product_busket_item_id)
        productt.product_stock -= item.quantity
        productt.save()
    #clear cart
    busketItems.objects.filter(user=current_user).delete()
    #send mail to customer
    mail_subject = 'Congratulation your order has set successfully'
    mail_body = render_to_string('orders/orderset.html', {
        'user': current_user,
        'order_number': order ,

    })
    to_email = current_user.email
    send_mail = django.core.mail.EmailMessage(mail_subject, mail_body, to=[to_email])
    send_mail.send()
    # send data to invoice
    data ={
        'order_number':order.order_number,
        'transID': payment.payment_id,
    }
    return JsonResponse(data)
def order_complete(request):
    order_number = request.GET.get('order_number')
    payment_id = request.GET.get('payment_id')
    try:
        order = Order.objects.get(order_number=order_number, is_ordered=True)
        order_Poduct = orderPoduct.objects.filter(order_id=order.id)
        payment = Payment.objects.get(payment_id=payment_id)
        Sub_Total = 0
        for i in order_Poduct:
            Sub_Total += i.product_price * i.quantity

        context={
            'order':order,
            'order_Poduct':order_Poduct,
            'order_number':order_number,
            'payment_id':payment,
            'Sub_Total':Sub_Total
        }
        return render(request, 'orders/order_complete.html', context)
    except(Order.DoesNotExist,Payment.DoesNotExist):
        return redirect('home')








