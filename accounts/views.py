from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


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


def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    context = {
        "form": None,
        "btn_label": "Click to logout",
        "title": "Logout page",
        "description": "You can always log back in at any time."
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