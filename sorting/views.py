import pandas as pd
import random
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from . import forms
from .models import PersonalInfo
# from sorting_library.random import testFunc
# Create your views here.
def startPage(request:HttpRequest,*args,**kwargs):
    return render(request,"home/home.html",{})

def contactPage(request:HttpRequest,*args,**kwargs):
    return render(request,"contact/contact.html",{})

def aboutPage(request:HttpRequest,*args,**kwargs):
    return render(request,"about/about.html",{})

@login_required(login_url='/login')
def registrationPage(request:HttpRequest,*args,**kwargs):
    if request.method == 'POST':
        form = forms.PersonalInfoForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.missionary = request.user
            info.save()
            return redirect('start-page')
    else:
        form = forms.PersonalInfoForm()
    return render(request,"registration_page/registration_page.html",{"form":form})

def signUpView(request:HttpRequest,*args,**kwargs):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
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

def logoutView(request:HttpRequest,*args,**kwargs):
    if request.method == 'POST':
        logout(request)
        return redirect('start-page')
    
def uploadExcelView(request:HttpRequest,*args,**kwargs):
    if request.method == 'POST':
        form = forms.ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)
            df.columns = df.columns.str.strip().str.lower()
            for _, row in df.iterrows(): 
                name = row.get('name')
                gender = row.get('gender')
                year_group = row.get('year_group')
                campus_church = row.get('campus_church')
                print(f'Name: {name}, Gender: {gender}, Year Group: {year_group}, Campus/Church: {campus_church}')
                PersonalInfo.objects.update_or_create(
                    name=name,
                    defaults={
                        'gender': gender,
                        'year_group': year_group,
                        'campus_church': campus_church,
                    }
                )
            return redirect('upload-excel-page')
                
    else:
        form = forms.ExcelUploadForm()
    return render(request,"sorting/upload_excel.html",{"form":form})

def randomGrouping(request:HttpRequest,*args,**kwargs):
    # Fetch all records as a list
    all_records = list(PersonalInfo.objects.all())
    # Shuffle the list randomly
    random.shuffle(all_records)
    # Split into 5 groups as evenly as possible
    group_size = len(all_records) // 5
    remainder = len(all_records) % 5
    groups = []
    start = 0
    for i in range(5):
        end = start + group_size + (1 if i < remainder else 0)
        groups.append(all_records[start:end])
        start = end
    return render(request, 'sorting/random_groups.html', {'groups': groups})