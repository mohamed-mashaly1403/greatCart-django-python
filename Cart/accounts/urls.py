from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('resetPassordPage/', views.resetPassordPage, name='resetPassordPage'),
    path('myOrders/', views.myOrders, name='myOrders'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    # path for order details
    path('order_details/<int:order_id>', views.order_details, name='order_details'),
    path('resetPasswordValidate/<uidb64>/<token>/', views.resetPasswordValidate, name='resetPasswordValidate'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),




]
