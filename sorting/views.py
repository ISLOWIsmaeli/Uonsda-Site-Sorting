from django.shortcuts import render
from django.http import HttpRequest
# from sorting_library.random import testFunc
# Create your views here.
def startPage(request:HttpRequest,*args,**kwargs):
    return render(request,"sorting/home.html",{})

def contactPage(request:HttpRequest,*args,**kwargs):
    return render(request,"sorting/contact.html",{})

def aboutPage(request:HttpRequest,*args,**kwargs):
    return render(request,"sorting/about.html",{})