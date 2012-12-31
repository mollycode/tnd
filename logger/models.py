from django.db import models
from django.contrib.auth.models import User

from courses.models import Course
from quizzes.models import Quiz, Question, Answer

class UserVisit(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add = True)
    
class UserViewsCourse(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    timestamp = models.DateTimeField(auto_now_add = True)
    
class UserViewsQuiz(models.Model):
    user = models.ForeignKey(User)
    quiz = models.ForeignKey(Quiz)
    timestamp = models.DateTimeField(auto_now_add = True)
    
class UserAnswersQuestion(models.Model):
    user = models.ForeignKey(User)
    quiz = models.ForeignKey(Quiz)
    answer = models.ForeignKey(Answer)
    is_correct = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add = True)