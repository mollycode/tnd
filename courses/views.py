# Create your views here.

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from courses.models import Instructor, Course, Night, Clip

def course(request, course_id, night_num, clip_num):
    course_id = int(course_id)
    night_num = int(night_num)
    clip_num = int(clip_num)
    
    td = {}
    td['course_id'] = course_id
    td['night_num'] = night_num
    td['clip_num'] = clip_num
    
    course = Course.objects.get(pk = course_id)
    td['course'] = course

    instructor = Instructor.objects.get(pk = course.instructor.pk)
    td['instructor'] = instructor

    try:
        night = Night.objects.get(course = course_id, night_num = night_num)
        td['night'] = night
        
        clip = Clip.objects.get(course_night = night.pk, clip_num = clip_num)
        td['clip'] = clip
        
        other_clips = Clip.objects.filter(course_night = night.pk)
        youtube_ids = []
        for other_clip in other_clips:
            # extract 11 char video id
            youtube_ids.append(other_clip.get_youtube_id())
        td['youtube_ids'] = youtube_ids
        
    except ObjectDoesNotExist as e:
        print "No nights, or clips don't exist\n"

    return render(request, "course.html", td)

def info(request, course_id):
    course_id = int(course_id)
    
    td = {}
    td['course_id'] = course_id
    
    course = Course.objects.get(pk = course_id)
    
    td['course'] = course
    
    try:
        td['night_1'] = Night.objects.get(course = course_id, night_num = 1)
        td['night_2'] = Night.objects.get(course = course_id, night_num = 2)
        td['night_3'] = Night.objects.get(course = course_id, night_num = 3)
    except ObjectDoesNotExist as e:
        print "No nights available yet"
        
    td['instructor'] = Instructor.objects.get(pk = course.instructor.pk)

    return render(request, "info.html", td)

def bare_course(request, course_id):
    return redirect("/course/%d/info/" % int(course_id))

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