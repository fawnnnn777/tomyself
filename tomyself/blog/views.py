from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . models import User, Thought
from datetime import datetime



@login_required(login_url='login/')
def index(request):
    thoughts = Thought.objects.all()
    context = {
        'thoughts': thoughts.order_by("-datetime").all
    }
    return render(request, 'blog/index.html', context)

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

def post(request):
    if request.method == "POST":
        user = request.user
        thought = request.POST['thought']
        new_thought = Thought(user=user, text=thought, datetime=datetime.now())
        new_thought.save()
        return HttpResponseRedirect(reverse('index'))

def profile(request):
    if request.method == "POST":
        bio = request.POST['bio']
        user = User.objects.get(username=request.user)
        user.biography = bio
        user.save()
        return HttpResponseRedirect(reverse('profile'))
    thoughts = Thought.objects.filter(user=request.user)
    user = User.objects.get(username=request.user)
    return render(request, 'blog/profile.html',{
        'user': user,
        'thoughts': thoughts
    })

def like(request, id):
    if request.method == "POST":
        thought = Thought.objects.get(id=id)
        thought.likes.add(request.user)
        thought.save()
        return HttpResponseRedirect(reverse('index'))
    
def delete(request, id):
    thought = Thought.objects.get(id=id)
    thought.delete()
    return HttpResponseRedirect(reverse('index'))


# Create your views here.
