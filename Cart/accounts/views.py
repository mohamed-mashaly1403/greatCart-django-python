from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
import django.core.mail
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .forms import regForm
from .models import account
from django.contrib.auth import authenticate

# Create your views here.

def register(request):
    if request.method == 'POST':
        print('wasl1')
        form = regForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print(form.errors)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            # username = email
            user = account.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password,username=username)
            user.phone = phone
            user.save()
            current_site = get_current_site(request)
            mail_subject ='great cart-activate your account'
            mail_body = render_to_string('accounts/emailActivation.html',{
                'user':user,
                'current_site':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_mail = django.core.mail.EmailMessage(mail_subject, mail_body, to=[to_email])
            send_mail.send()
            messages.success(request,'Registration done')


            return redirect('register')

        else:
            print('not vaild')
    else:
        print('not post')
        form = regForm()
    context ={
        'form':form
    }
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'login done')
            return redirect('home')
        else:
            messages.error(request,'invaild login')
            return redirect('login')
    return render(request,'accounts/login.html')
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'logout done')
    return redirect('login')
