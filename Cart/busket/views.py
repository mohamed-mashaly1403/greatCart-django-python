from django.shortcuts import render,redirect,get_object_or_404
from store.models import product
from .models import  buskett ,busketItems
from django.core.exceptions import ObjectDoesNotExist




def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
        # int(request.POST['product'])
    return cart
def add_Cart(request,product_id):
    products = product.objects.get(id=product_id)
    try:
        cart = buskett.objects.get(cart_id = _cart_id(request))
    except buskett.DoesNotExist:
        cart = buskett.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()
    try:
        cart_item = busketItems.objects.get(product_busket_item=products,busket_item=cart)

        cart_item.quantity += 1


    except busketItems.DoesNotExist:
        cart_item = busketItems.objects.create(
            product_busket_item=products,
            busket_item=cart,
            quantity = 1
        )
    cart_item.save()
    return redirect('busket')

def remove_cart(request,product_id):
    cart = buskett.objects.get(cart_id=_cart_id(request))
    productt = get_object_or_404(product,id=product_id)
    cartItem = busketItems.objects.get(product_busket_item=productt,busket_item=cart)
    if cartItem.quantity > 1:
        cartItem.quantity -= 1
        cartItem.save()
        return redirect('busket')
    else:
        cartItem.delete()
        return redirect('busket')
def remove_cart_item(request,product_id):
    cart = buskett.objects.get(cart_id=_cart_id(request))
    productt = get_object_or_404(product, id=product_id)
    cartItem = busketItems.objects.get(product_busket_item=productt, busket_item=cart)
    cartItem.delete()
    return redirect('busket')






def busket(request,total=0,quantity=0,cart_items=None):
    try:

        cart = buskett.objects.get(cart_id=_cart_id(request))
        cart_items = busketItems.objects.filter(busket_item=cart,busketItems_is_active=True)
        for cart_item in cart_items:
            quantity += cart_item.quantity
            total += int(cart_item.product_busket_item.product_price) * int(cart_item.quantity)
        tax = (0.02 * total)
        Gtotal = total + tax
    except ObjectDoesNotExist:
        pass
    context ={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax': tax,
        'Gtotal':Gtotal
    }

    return render(request,'store/busket.html',context)

# Create your views here.
