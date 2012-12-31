from django.contrib import admin
from logger.models import Instructor, Course, Night, Clip

admin.site.register(UserVisit)
admin.site.register(UserViewsCourse)
admin.site.register(UserViewsQuiz)
admin.site.register(UserAnswersQuestion)