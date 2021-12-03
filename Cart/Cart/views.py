from django.shortcuts import render
from store.models import product,RatingReview




def home(request):
    products = product.objects.all().filter( product_is_available=True).order_by('-product_created_date')
    reviews =None
    for Product in products:
        reviews = RatingReview.objects.filter(product_id=Product.id,status=True)
        # do nothing

    context = {
        'products':products,
        'reviews':reviews
    }
    return render(request,'home.html',context)
