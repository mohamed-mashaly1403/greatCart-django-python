from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from store.models import product,variation
from .models import  buskett ,busketItems
from django.core.exceptions import ObjectDoesNotExist




def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
        # int(request.POST['product'])
    return cart
def add_Cart(request,product_id):
    current_user = request.user
    products = product.objects.get(id=product_id)
    if current_user.is_authenticated:
        var_product = []
        if request.method == 'POST':
            for key in request.POST:
                value = request.POST[key]
                try:
                    var = variation.objects.get(product=products, variation_category__iexact=key,
                                                variation_value__iexact=value)
                    var_product.append(var)
                except:
                    pass


        is_cart_item_exists = busketItems.objects.filter(product_busket_item=products, user=current_user).exists()
        if is_cart_item_exists:
            cart_item = busketItems.objects.filter(product_busket_item=products, user=current_user)
            ex_vr_list = []
            id = []
            for itemm in cart_item:
                ex_vr = itemm.variations.all()
                ex_vr_list.append(list(ex_vr))
                id.append(itemm.id)
            if var_product in ex_vr_list:
                index = ex_vr_list.index(var_product)
                item_id = id[index]
                item = busketItems.objects.get(product_busket_item=products, id=item_id)
                item.quantity += 1
                item.save()

            else:
                item = busketItems.objects.create(
                    product_busket_item=products,
                    user=current_user,
                    quantity=1
                )
                if len(var_product) > 0:
                    item.variations.clear()
                    item.variations.add(*var_product)
                item.save()

        else:
            cart_item = busketItems.objects.create(
                product_busket_item=products,
                user=current_user,
                quantity=1
            )
            if len(var_product) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*var_product)
            cart_item.save()
        return redirect('busket')
      #==================================

    else:
        var_product =[]
        if request.method == 'POST':
            for key in request.POST:
                value = request.POST[key]
                try:
                    var = variation.objects.get(product=products, variation_category__iexact= key,variation_value__iexact=value)
                    var_product.append(var)
                except:
                    pass

        try:
            cart = buskett.objects.get(cart_id = _cart_id(request))
        except buskett.DoesNotExist:
            cart = buskett.objects.create(
                cart_id=_cart_id(request)
            )
        cart.save()
        is_cart_item_exists = busketItems.objects.filter(product_busket_item=products,busket_item=cart).exists()
        if is_cart_item_exists:
            cart_item = busketItems.objects.filter(product_busket_item=products,busket_item=cart)
            ex_vr_list =[]
            id = []
            for itemm in  cart_item:
                ex_vr = itemm.variations.all()
                ex_vr_list.append(list(ex_vr))
                id.append(itemm.id)
            if  var_product in  ex_vr_list:
                index = ex_vr_list.index(var_product)
                item_id = id[index]
                item = busketItems.objects.get(product_busket_item=products,id=item_id)
                item.quantity += 1
                item.save()

            else:
                item =  busketItems.objects.create(
                product_busket_item=products,
                busket_item=cart,
                quantity = 1
            )
                if len(var_product) >0:
                    item.variations.clear()
                    item.variations.add(*var_product)
                item.save()

        else :
            cart_item = busketItems.objects.create(
                product_busket_item=products,
                busket_item=cart,
                quantity = 1
            )
            if len(var_product) >0:
                cart_item.variations.clear()
                cart_item.variations.add(*var_product)
            cart_item.save()
        return redirect('busket')

def remove_cart(request,product_id,cart_id):

    productt = get_object_or_404(product,id=product_id)
    try:
        if request.user.is_authenticated:
            cartItem = busketItems.objects.get(product_busket_item=productt,user=request.user, id=cart_id)
        else:
            cart = buskett.objects.get(cart_id=_cart_id(request))
            cartItem = busketItems.objects.get(product_busket_item=productt,busket_item=cart,id=cart_id)
        if cartItem.quantity > 1:
            cartItem.quantity -= 1
            cartItem.save()
            return redirect('busket')
        else:
            cartItem.delete()
            return redirect('busket')
    except:
        pass

def remove_cart_item(request,product_id,cart_id):
    productt = get_object_or_404(product, id=product_id)
    if request.user.is_authenticated:
        cartItem = busketItems.objects.get(product_busket_item=productt, user=request.user, id=cart_id)
    else:
        cart = buskett.objects.get(cart_id=_cart_id(request))
        cartItem = busketItems.objects.get(product_busket_item=productt, busket_item=cart,id=cart_id)
    cartItem.delete()
    return redirect('busket')






def busket(request,total=0,quantity=0,cart_items=None):
    tax = 0
    Gtotal = 0
    try:
        if request.user.is_authenticated:
            cart_items = busketItems.objects.filter(user=request.user, busketItems_is_active=True)
        else:
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
@login_required(login_url='login')
def checkout(request,total=0,quantity=0,cart_items=None):
    tax = 0
    Gtotal = 0
    try:

        if request.user.is_authenticated:
            cart_items = busketItems.objects.filter(user=request.user, busketItems_is_active=True)
        else:
            cart = buskett.objects.get(cart_id=_cart_id(request))
            cart_items = busketItems.objects.filter(busket_item=cart,busketItems_is_active=True)
        for cart_item in cart_items:
            quantity += cart_item.quantity
            total += int(cart_item.product_busket_item.product_price) * int(cart_item.quantity)
        tax = (0.02 * total)
        Gtotal = total + tax
    except ObjectDoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'Gtotal': Gtotal
    }
    return render(request,'store/checkout.html',context)