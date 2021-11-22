from django.shortcuts import render, get_object_or_404
from store.models import product
from cat.models import cat
from busket.models import busketItems,buskett
from busket.views import _cart_id
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from django.db.models import Q
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
    context ={'single':single,
              'stock': stock,
              'inCart':inCart,
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
