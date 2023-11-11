from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import authenticate,login
from django.contrib import messages

def home(request):
    return render(request,'home.html')


def login_page(request):
    try:
        if request.method=="POST":
            username=request.POST.get('username')
            passward=request.POST.get('passward')
            try:
                u=CustomUser.objects.get(username=username)
                user=authenticate(request,username=username,passward=passward)
                if user is not None:
                    login(request,user)
                    return redirect('')
                else:
                    messages.error(request, "Your is passward incorect")
                    return redirect('/login/')
            except:
                messages.error(request,'User id is not found.')
                return redirect('/login/')
    except u.DoesNotExist:
        return redirect('/login/')
    return render(request,'login_page.html')
# Create your views here.






def reg(request):
    try:
        if request.method=="POST":
            username=request.POST.get('username')
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            password=request.POST.get('passward')
            confirm_password=request.POST.get('confirm_passward')
            phone_number=request.POST.get('phone_number')
            
            if password==confirm_password:
                print('open')
                
                User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password,phone_number=phone_number)
                print('close')
                
                return redirect('/login/')
                
    except:
        print('pass')
        pass
    return render(request,'registration.html')

