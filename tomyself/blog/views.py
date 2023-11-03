from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . models import User

@login_required(login_url='login/')
def index(request):
    return render(request, 'blog/index.html')

def login_view(request):
    if request.method == "GET":
        return render(request, 'blog/login.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else: 
            return render(request, 'blog/register.html')
        
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'blog/register.html',{
                "message": "password confirmation doesn't match"
            })
        try: 
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError: 
            return render(request, 'blog/register.html',{
                "message": "username already taken"
            })
        login(request, user)
        return HttpResponse("you are good!")
    return render(request, 'blog/register.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Create your views here.
