from django.contrib import admin
from courses.models import Instructor, Course, Night, Clip

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Night)
admin.site.register(Clip)