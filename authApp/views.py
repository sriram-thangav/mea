from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate

def register(request):
    return render(request,'authApp/register.html')

def login(request):
    return render(request,'authApp/login.html')

def logout(request):
    return render(request,'authApp/register.html')
