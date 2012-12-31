from django.db import models

from courses.models import Clip

class Quiz(models.Model):
    clip = models.ForeignKey(Clip)
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    text = models.TextField()
    
class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    is_correct_answer = models.BooleanField()