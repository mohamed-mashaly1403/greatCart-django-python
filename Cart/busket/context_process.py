from .models import buskett,busketItems
from .views import _cart_id
def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = buskett.objects.filter(cart_id=_cart_id(request))
            cart_items = busketItems.objects.all().filter(busket_item=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except buskett.DoesNotExist:
            cart_count = 0
    return dict( cart_count= cart_count)

