from django.contrib import admin
from courses.models import Instructor, Course, CourseNight, Clip

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(CourseNight)
admin.site.register(Clip)