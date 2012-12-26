# Create your views here.

from django.shortcuts import render

def course(request):
    return render(request, "course.html")

# temporary course pages

def cambron(request):
    return render(request, "cambroncourseinfo.html")

def cioffi(request):
    return render(request, "ciofficourseinfo.html")

def fox(request):
    return render(request, "foxcourseinfo.html")

def glass(request):
    return render(request, "glasscourseinfo.html")