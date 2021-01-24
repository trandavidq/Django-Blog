from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from .models import blog_post
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
    
    if user is not None:
        auth_login(request, user)
        context= {
        'user':user,
        'user_posts':user.blog_post_set.all(),
    }
        return render(request,'blog/home.html',context)
        
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("Login unsuccessful")
    
def signup(request):
    return render(request,'blog/signup.html')

def register(request):
    #registers the user from the signup. POST requests from signup.html go here
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(username=username, password=password)
    if user is not None:
        #user is already in db, so redirect to login page
        print('Existing user')
        context={
            'uName':user.username,
            'pWord':user.password,
        }
        return render(request,'blog/login.html',context)

        
    else:
        #create and register new user, go to homepage
        new_user=User.objects.create_user(username=username,password=password)
        context={
            'user':new_user,
            'user_posts':new_user.blog_post_set.all(),
        }
        auth_login(request, new_user)
        return render(request,'blog/home.html',context)

    

def logout(request):
    auth_logout(request)
    return redirect('blog:login')

def home(request):
    return render(request,'blog/home.html')

def post(request):
    post_title = request.POST['title']
    post_body = request.POST['body']
    author= request.user
    post = blog_post.objects.create(user=author,title=post_title,body=post_body)
    context={
        'user':author,
        'user_posts':author.blog_post_set.all(),
    }
    return render(request,'blog/home.html',context)

def delete(request):
    #delete the selected post
    user=request.user
    return HttpResponse("Delete (work on)")
