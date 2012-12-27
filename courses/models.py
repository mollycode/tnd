from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    professor = models.ForeignKey(User)
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000)
    
    def __unicode__(self):
        return self.title
    
class CourseNight(models.Model):
    course = models.ForeignKey(Course)
    night = models.IntegerField()
    
    def __unicode__(self):
        return str(self.course) + ": " + str(self.night)

class Clip(models.Model):
    course_night = models.ForeignKey(CourseNight)
    youtube_video = models.URLField()
    clip_num = models.IntegerField()
    
    """
    def __unicode__(self):
        return course_night.course + ": " + course_night.night + " - clip " + self.clip_num
        """