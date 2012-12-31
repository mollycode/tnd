from django.contrib import admin
from logger.models import UserVisit, UserViewsCourse, UserViewsQuiz, UserAnswersQuestion

admin.site.register(UserVisit)
admin.site.register(UserViewsCourse)
admin.site.register(UserViewsQuiz)
admin.site.register(UserAnswersQuestion)