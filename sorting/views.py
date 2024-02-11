from django.shortcuts import render
from django.http import HttpRequest
from sorting_library.random import testFunc
# Create your views here.
def startpage(request:HttpRequest,*args,**kwargs):
    print(testFunc(3))
    return render(request,"sorting/home.html",{})