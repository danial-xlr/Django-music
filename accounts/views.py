from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UserLoginForm , UserRegisterationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User


def user_login(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, 'You logged in successfully','success')
                return redirect('home')
            else:
                messages.error(request,'Wrong Username or Password','danger')
    else:   
        form =UserLoginForm()
    return render(request,'accounts/login.html',{'form':form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'],cd['email'],cd['password1'])
            messages.success(request,'You register succesfully','success')
            return redirect('user_login')
    else:
        form = UserRegisterationForm()
    return render(request,'accounts/register.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,'You Logout Succesfully','success')
    return redirect('home')

def contact(request):
    return render(request,'accounts/contact.html')