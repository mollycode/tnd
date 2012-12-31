# Create your views here.

from django.shortcuts import render, redirect

def get_out(request):
    return redirect("main.views.home")