from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from sorting_library.random import testFunc
# Create your views here.
def startPage(request:HttpRequest,*args,**kwargs):
    return render(request,"home/home.html",{})

def contactPage(request:HttpRequest,*args,**kwargs):
    return render(request,"contact/contact.html",{})

def aboutPage(request:HttpRequest,*args,**kwargs):
    return render(request,"about/about.html",{})

def registrationPage(request:HttpRequest,*args,**kwargs):
    return render(request,"registration_page/registration_page.html",{})

def signUpView(request:HttpRequest,*args,**kwargs):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start-page')
    else:
        form=UserCreationForm()
    return render(request,"signup/signup.html",{"form":form})

def loginView(request:HttpRequest,*args,**kwargs):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('start-page')
    else:
        form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})

# def loginView(request:HttpRequest,*args,**kwargs):
#     if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         context={'error_message':'Invalid username or password.'}
#         user= authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('success')
#         else:
#             return render(request, 'sorting/login.html',context)
#     else:
#         return render(request, 'login.html')
    
# def signUpView(request:HttpRequest,*args,**kwargs):
#     if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         context = {'error_message':'Username already exists. Please choose a different one.'}
#         if User.objects.filter(username=username).exists():
#             return render(request,'sorting/signup.html',context)
#         else:
#             user = User.objects.create_user(username=username, password=password)
#             login(request,user)
#             return redirect('success')
#     else:
#         return render(request,'signup.html')
