from django.urls import path
from . import views

urlpatterns = [

    path('', views.busket, name='busket'),
    path('add_cart/<int:product_id>/', views.add_Cart, name='addCart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),


]
