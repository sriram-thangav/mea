from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from  .forms import LoginForm
from django.http import HttpResponse

def register(request):
    return render(request,'authApp/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is None:
            return HttpResponse('invalid credentials')
        
        login(request,user)
        return HttpResponse('success')
    else:
        form = LoginForm()
        return render(request,'authApp/login.html',{'form':form})

def logout(request):
    return render(request,'authApp/register.html')
