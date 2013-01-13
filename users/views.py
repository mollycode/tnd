# Create your views here.

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from users.forms import UserProfileForm, UserCreationForm, UserRegistrationForm, UserEmailForm
from courses.forms import CourseRatingForm
from users.models import get_or_create_user_profile, UserProfile

from courses.models import Course

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
    td = {}
    
    profile_form = UserProfileForm()
    email_form = UserEmailForm(instance = request.user)
    
    if request.POST:
        try:
            profile_form = UserProfileForm(request.POST, instance = request.user.get_profile())
            email_form = UserEmailForm(request.POST, instance = request.user)
        except:
            profile_form = UserProfileForm(request.POST)
            email_form = UserEmailForm(request.POST, instance = request.user)
        
        if profile_form.is_valid() and email_form.is_valid():
            user_profile = profile_form.save(commit = False)
            user_profile.user = request.user
            user_profile.save()
            
            email_form.save()
            
    else:
        try:
            profile = get_or_create_user_profile(request)
            profile_form = UserProfileForm(instance = profile)
        except:
            print sys.exc_info()[0]
            td["creating_profile"] = True
            
    td["profile_form"] = profile_form
    td["email_form"] = email_form
    td["is_profile_page"] = True
    
    return render(request, "profile.html", td)

def register(request):
    if request.user.is_authenticated():
        return redirect("users.views.profile")
    
    if request.POST:
        creation_form = UserCreationForm(request.POST)
        profile_form = UserRegistrationForm(request.POST)
        
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
        profile_form = UserRegistrationForm()
    return render(request, "register.html", {
                                             "creation_form": creation_form,
                                             "profile_form": profile_form
                                             })

@login_required
def currentlessons(request):
    user_profile = UserProfile.objects.get(user = request.user)
    courses = user_profile.current_courses.all()
    
    td = {}
    td["courses"] = courses
    td["is_profile_page"] = True
    
    return render(request, "currentlessons.html", td)

@login_required
def completedcourses(request):
    
    rating_form = CourseRatingForm()

    td = {}
    td["courses"] = []
    td["is_profile_page"] = True
    td["rating_form"] = rating_form

    if request.POST:
        rating_form = CourseRatingForm(request.POST)
        
        if rating_form.is_valid():
            rating_form.save()
            return redirect("/")
    
    return render(request, "completedcourses.html", td)

@login_required
def recommended(request):
    courses = Course.objects.all()

    td = {}
    td["courses"] = courses
    return render(request, 'recommended.html', td)

@login_required
def addcourse(request, course_id):
    course_id = int(course_id)
    
    if request.GET:
        if request.GET["next"]:
            next = request.GET["next"]
            
    else:
        next = "/course/%d/info/" % course_id
    
    user_profile = UserProfile.objects.get(user = request.user)
    course = Course.objects.get(pk = course_id)
    user_profile.current_courses.add(course)
    user_profile.save()
    
    return redirect(next)

@login_required
def removecourse(request, course_id):
    course_id = int(course_id)
    
    if request.GET:
        if request.GET["next"]:
            next = request.GET["next"]
            
    else:
        next = "/users/currentlessons/"
    
    user_profile = UserProfile.objects.get(user = request.user)
    course = Course.objects.get(pk = course_id)
    # try:
    user_profile.current_courses.remove(course)
    # except ObjectDoesNotExist as e:
    user_profile.save()
    
    return redirect(next)

def finishcourse(request, course_id):
    return redirector(request)

def logout(request):
    auth_logout(request)
    return redirect("/")

def redirector(request):
    return redirect("users.views.profile")


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