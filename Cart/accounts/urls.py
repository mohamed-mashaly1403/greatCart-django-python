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
    path('resetPasswordValidate/<uidb64>/<token>/', views.resetPasswordValidate, name='resetPasswordValidate'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),




]
