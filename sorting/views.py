from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.contrib.auth.models import User
# from sorting_library.random import testFunc
# Create your views here.
def startPage(request:HttpRequest,*args,**kwargs):
    return render(request,"sorting/home.html",{})

def contactPage(request:HttpRequest,*args,**kwargs):
    return render(request,"sorting/contact.html",{})

def aboutPage(request:HttpRequest,*args,**kwargs):
    return render(request,"sorting/about.html",{})

def loginView(request:HttpRequest,*args,**kwargs):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        context={'error_message':'Invalid username or password.'}
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('success')
        else:
            return render(request, 'login.html',context)
    else:
        return render(request, 'login.html')
    
def signUnView(request:HttpRequest,*args,**kwargs):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filer(username=username).exists():
            return render(request,'signup.html',{'error_message':'Username already exists. Please choose a different one.'})
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request,user)
            return redirect('success')
    else:
        return(request,'signup.html')
