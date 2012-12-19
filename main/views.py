# Create your views here.

from django.shortcuts import render

from django.contrib.auth import authenticate, login

def home(request):
    return render(request, "index.html")

def personalpage(request):
    return render(request, "personalpage.html")

def about(request):
    return render(request, "about.html")

def courses(request):
    return render(request, "courses.html")

def wiki(request):
    return render(request, "wiki.html")

