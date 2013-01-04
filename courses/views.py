# Create your views here.

from django.shortcuts import render, redirect

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

    night = Night.objects.get(course = course_id, night_num = night_num)
    td['night'] = night
    
    try:
        clip = Clip.objects.get(course_night = night.pk, clip_num = clip_num)
        td['clip'] = clip
        
        other_clips = Clip.objects.filter(course_night = night.pk)
        youtube_ids = []
        for other_clip in other_clips:
            # extract 11 char video id
            youtube_ids.append(other_clip.youtube_video[29:29+11])
        td['youtube_ids'] = youtube_ids
    except DoesNotExist as e:
        print "clips don't exist"

    return render(request, "course.html", td)

def info(request, course_id):
    course_id = int(course_id)
    
    td = {}
    td['course_id'] = course_id
    
    course = Course.objects.get(pk = course_id)
    
    td['course'] = course
    td['night_1'] = Night.objects.get(course = course_id, night_num = 1)
    td['night_2'] = Night.objects.get(course = course_id, night_num = 2)
    td['night_3'] = Night.objects.get(course = course_id, night_num = 3)
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