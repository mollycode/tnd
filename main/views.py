from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "index.html")

@login_required
def personalpage(request):
    return render(request, "personalpage.html")

def about(request):
    return render(request, "about.html")

def difference(request):
    return render(request, "difference.html")

def team(request):
    return render(request, "team.html")

def courselist(request):
    td = {}
    td['is_courselist_page'] = True
    return render(request, "courselist.html", td)

def wiki(request):
    return redirect("main.views.home")

def register(request):
    return redirect("users.views.register")
