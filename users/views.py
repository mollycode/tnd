# Create your views here.

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from forms import UserProfileForm
from models import get_or_create_user_profile

import sys

def login(request):
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
                return redirect("users.views.profile")
            else:
                # print "not an active user"
                return render(request, "login.html")

    else:
        return render(request, "login.html")

@login_required
def profile(request):
    template_dict = {}
    
    form = UserProfileForm()
    
    if request.POST:
        form = UserProfileForm(request.POST, instance = request.user.get_profile())
        if form.is_valid():
            user_profile = form.save(commit = False)
            user_profile.user = request.user
            user_profile.save()
            
    else:
        try:
            profile = get_or_create_user_profile(request)
            form = UserProfileForm(instance = profile)
        except:
            print sys.exc_info()[0]
            template_dict["creating_profile"] = True
            
    template_dict["form"] = form
    
    return render(request, "profile.html", template_dict)

"""
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
    """

def register(request):
    if request.POST:
        creation_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if creation_form.is_valid() and profile_form.is_valid():
            
            assert creation_form.cleaned_data.get("password1") == creation_form.cleaned_data.get("password2")
            
            new_user = creation_form.save(commit = False)
            new_profile = profile_form.save(commit = False)

            new_user.save()
            new_profile.user = new_user
            new_profile.save()
            
            return login(request)
    else:
        creation_form = UserCreationForm()
        profile_form = UserProfileForm()
    return render(request, "register.html", {
                                             "creation_form": creation_form,
                                             "profile_form": profile_form
                                             })

def logout(request):
    auth_logout(request)
    return redirect("/")