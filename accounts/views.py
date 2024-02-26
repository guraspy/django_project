from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import DetailView
from django.contrib.auth.models import User
from tweets.models import Tweet
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def user_profile_view(request, username, *args, **kwargs): 
    
    profile_user = username
    #another way to get profile_user from 'profile/<str:username>/' in urls
    # profile_user = kwargs['username']
    
    data = Tweet.objects.filter(user__username=profile_user)
    
    # reversing data to display new tweets first
    tweets = {    
        "tweets": reversed(data),
        "profile_user": profile_user
    } 

    return render(request, "accounts/profile.html", tweets)



def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("/")
    context = {
        "form": form,
        "btn_label": "Click to login",
        "title": "Login page"
    }
    return render(request, "accounts/auth.html", context)

@login_required
def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    context = {
        "form": None,
        "btn_label": "Click to logout",
        "title": "Logout page",
        "description": "You can always log back in at any time.",
        "logout":True
    }
    return render(request, "accounts/auth.html", context )
    

def register_view(request, *Args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password1"))
        login(request, user)
        return redirect("/")
    context = {
        "form": form,
        "btn_label": "Click to register",
        "title": "Register page"
    }
    return render(request, "accounts/auth.html", context)
