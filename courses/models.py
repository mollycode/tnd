import os

from django.db import models
from django.contrib.auth.models import User
  
def get_course_image_path(instance, filename):
    return os.path.join('courses', str(instance.id), filename)

def get_instructor_image_path(instance, filename):
    return os.path.join('instructors', str(instance.id), filename)

class Instructor(models.Model):
    name = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    user = models.ForeignKey(User, null = True, blank = True)
    image = models.ImageField(upload_to = get_instructor_image_path, null = True, blank = True)
    about = models.TextField(null = True, blank = True)
    
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name

class Course(models.Model):

    CATEGORIES = (
        ('HI', 'history'),
        ('MA', 'math'),
        ('SC', 'science'),
        ('LI', 'literature'),
        ('TE', 'technology'),
        ('FI', 'finance'),
        ('MI', 'miscellaneous'),
    )

    RATINGS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    instructor = models.ForeignKey(Instructor)
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(upload_to = get_course_image_path, null = True, blank = True)
    category = models.CharField(max_length=3, choices=CATEGORIES)
    available = models.BooleanField()
    release_date = models.DateField(null = True, blank = True)
    release_string = models.CharField(max_length = 100, null = True, blank = True)
    rating = models.DecimalField(null = True, decimal_places = 2, max_digits = 3, choices=RATINGS)
    num_rating = models.IntegerField(default= 0)
    
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.title + " - " + str(self.instructor)
    
    def get_info_url(self):
        return "/course/%d/info/" % self.pk

    def __str__(self):
        return self.title + " - " + str(self.instructor)

class Night(models.Model):
    course = models.ForeignKey(Course)
    night_num = models.IntegerField()
    title = models.CharField(max_length = 200, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return str(self.course) + ": Night " + str(self.night_num)

class Clip(models.Model):
    course_night = models.ForeignKey(Night)
    clip_num = models.IntegerField()
    title = models.CharField(max_length = 200, null = True, blank = True)
    youtube_video = models.URLField()
    description = models.TextField(null = True, blank = True)
    
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return str(self.course_night) + ": Clip " + str(self.clip_num)
    
    def get_youtube_id(self):
        return self.youtube_video[29:29+11]

