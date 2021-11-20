from django.urls import path
from . import views

urlpatterns = [

    path('', views.busket, name='busket'),
    path('add_cart/<int:product_id>/', views.add_Cart, name='addCart'),


]
