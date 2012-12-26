# Create your views here.

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from forms import UserProfileForm

def login(request):
    if request.POST:
        return profile(request)
    else:
        return render(request, "login.html")

def profile(request):
    if request.POST:
        if 'password1' in request.POST:
            password = request.POST['password1']
        else:
            password = request.POST['password']
        username = request.POST['username']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                # request.session["user"] = user
                return render(request, "profile.html", {"username": username})
            else:
                print "not an active user"
                return render(request, "login.html")
        else:
            print "user is none"
    print "skipped it all"
    return render(request, "login.html")

def register(request):
    if request.POST:
        creation_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid():
            assert form.cleaned_data.get("password1") == form.cleaned_data.get("password2")
            new_user = User.objects.create_user(form.cleaned_data.get("username"), "email@gmail.com", form.cleaned_data.get("password1"))
            new_user.save()
            #new_profile = UserProfile.objects.create_user_profile
            return profile(request)
    else:
        creation_form = UserCreationForm()
        profile_form = UserProfileForm()
    return render(request, "register.html", {
                                             "creation_form": creation_form,
                                             "profile_form": profile_form})

def logout(request):
    auth_logout(request)
    return redirect("/")