from django.urls import path
from . import views

urlpatterns = [

    path('', views.store, name='store'),
    path('category/<slug:cat_slug>/', views.store, name='products_by_cat'),
    path('category/<slug:cat_slug>/<slug:product_slug>', views.product_details, name='product_details'),
    path('search', views.search, name='search'),

]
