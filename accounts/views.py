from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from tweets.models import Tweet
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.db.models import Sum

@login_required
def user_profile_view(request, username, *args, **kwargs): 
    
    profile_user = username
    #another way to get profile_user from 'profile/<str:username>/' in urls
    # profile_user = kwargs['username']
    
    data = Tweet.objects.filter(user__username=profile_user)
    profile = UserProfile.objects.get(user=request.user)
    
    likes = Tweet.objects.filter(user__username=profile_user).aggregate(total_likes=Sum('no_of_likes'))
    likes.get('no_of_likes')
    
    # reversing data to display new tweets first
    tweets = {    
        "tweets": reversed(data),
        "profile_user": profile_user,
        "profile": profile,
        "likes": likes
    } 

    return render(request, "accounts/profile.html", tweets)

@login_required
def edit_profile_view(request, username, *args, **kwargs): 
    try:
        profile_user = UserProfile.objects.get(user=request.user)
    except:
        # If UserProfile does not exist for the current request user
        user = User.objects.get(username=username)
        profile_user = UserProfile.objects.create(user_id=user.id)
        profile_user.save()

    if request.method == 'POST':
        if request.FILES.get('image') == None:
            image = profile_user.profileimg
            print("1")
        
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            print("2")
          
        bio = request.POST.get('bio')  
        name = request.POST.get('name').capitalize()
        surname = request.POST.get('surname').capitalize()
        
        profile_user.profileimg = image
        profile_user.bio = bio
        profile_user.name = name
        profile_user.surname = surname
        
        profile_user.save()
        
        return redirect("/profile/" + str(profile_user) + "/edit-profile/")

    return render(request, "accounts/edit-profile.html", {"profile_user": profile_user})



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
