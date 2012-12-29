# Create your views here.

from django.shortcuts import render, redirect

from courses.models import Course

def course(request, course_id, night, clip):
    td = {}
    td['course_id'] = int(course_id)
    td['night'] = int(night)
    td['clip'] = int(clip)

    return render(request, "course.html", td)

def info(request, course_id):
    td = {}
    td['course_id'] = int(course_id)
    td['course'] = Course.objects.get(pk = int(course_id))

    return render(request, "info.html", td)

def discussion(request):
    return redirect("main.views.home")

def get_out(request):
    return redirect("main.views.home")

# temporary course pages

def cambron(request):
    return render(request, "cambroncourseinfo.html")

def cioffi(request):
    return render(request, "ciofficourseinfo.html")

def fox(request):
    return render(request, "foxcourseinfo.html")

def glass(request):
    return render(request, "glasscourseinfo.html")