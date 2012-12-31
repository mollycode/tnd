from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "index.html")

@login_required
def personalpage(request):
    return render(request, "personalpage.html")

def about(request):
    return render(request, "about.html")

def team(request):
    return render(request, "team.html")

def courselist(request):
    return render(request, "courselist.html")

def wiki(request):
    return render(request, "wiki.html")

