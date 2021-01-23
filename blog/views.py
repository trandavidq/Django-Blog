from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
# Create your views here.
def login(request):
    return render(request,'blog/login.html')

def verify(request):
    #change: handles authentication
    username = request.POST['username']
    password = request.POST['password']
    print(username)
    print(password)
    user = authenticate(username=username, password=password)
    context= {
        'user':user,
    }
    if user is not None:
        auth_login(request, user)
        return render(request,'blog/home.html',context)
        
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("Login unsuccessful")
    
def signup(request):
    return render(request,'blog/signup.html')

def logout(request):
    auth_logout(request)
    return redirect('blog:login')
