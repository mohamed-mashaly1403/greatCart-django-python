from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from store.models import product,RatingReview, ProductGallery
from cat.models import cat
from busket.models import busketItems,buskett
from busket.views import _cart_id
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from django.db.models import Q
from .form import RatingReviewForm


from .models import ProductGallery
from orders.models import orderPoduct


def store(request,cat_slug=None):
    cate = None
    products = None

    if cat_slug != None:
        cate = get_object_or_404(cat,cat_slug= cat_slug)
        products = product.objects.all().filter(product_cat=cate,product_is_available=True)
        Paginatorr = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = Paginatorr.get_page(page)
        x = range(1, Paginatorr.num_pages)
        products_count = products.count()

    else:
        products = product.objects.all().filter(product_is_available=True).order_by('id')
        Paginatorr = Paginator(products,6)
        page = request.GET.get('page')
        paged_products =Paginatorr.get_page(page)
        x = range(1,  Paginatorr.num_pages)
        products_count = products.count()


    context = {'products': paged_products,
               'products_count':products_count,
               'x':x
               }
    return render(request,'store/store.html',context)
def product_details(request,cat_slug,product_slug):
    try:
        single = product.objects.get(product_cat__cat_slug=cat_slug,product_slug=product_slug)
        stock = int(single.product_stock)
        inCart = busketItems.objects.filter(busket_item__cart_id=_cart_id(request),product_busket_item=single).exists()

    except Exception as e:
        raise e
    try:
                Orderproduct = orderPoduct.objects.filter(user=request.user,product=single.id).exists()
    except (orderPoduct.DoesNotExist,TypeError):
        Orderproduct = None
    reviews = RatingReview.objects.filter(product_id=single.id,status=True)
    product_gallery = ProductGallery.objects.filter(product_id = single.id)
    context ={'single':single,
              'stock': stock,
              'inCart':inCart,
              'Orderproduct':Orderproduct,
              'reviews':reviews,
              'product_gallery':product_gallery
              }
    return render(request,'store/product_details.html',context)

# Create your views here.
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword != '':
            products = product.objects.order_by('-product_created_date').filter(Q(product_desc__icontains= keyword) | Q(product_name__icontains= keyword))
            productcount = products.count()
        else:
            products =''
            productcount = 0
    context = {
        'products': products,
        'products_count': productcount,
    }
    return render(request,'store/store.html',context)
def submit_review(request,product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = RatingReview.objects.get(user__id=request.user.id,product__id=product_id)
            form = RatingReviewForm(request.POST,instance=reviews)
            form.save()
            messages.success(request,'review has updated')
            return redirect(url)

        except RatingReview.DoesNotExist:
            form = RatingReviewForm(request.POST)
            if form.is_valid() :
                data = RatingReview()
                data.subject = form.cleaned_data['subject']
                data.review = form.cleaned_data['review']
                data.rating = form.cleaned_data['rating']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'review has submited')
            else:
                print('not vaild')

                return redirect(url)




