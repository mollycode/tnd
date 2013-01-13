from django.db import models
from django.contrib.auth.models import User

from courses.models import Course

from users.extras import CountryField

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    MALE = "M"
    FEMALE = "F"
    SEX_CHOICES = (
       (MALE, "Male"),
       (FEMALE, "Female")
    )
    
    HIGH_SCHOOL = "HS"
    ASSOCIATES = "2YR"
    BACHELORS = "4YR"
    MASTERS = "MS"
    PHD = "PHD"
    
    EDUCATION_CHOICES = (
        (HIGH_SCHOOL, "High school (secondary school)"),
        (ASSOCIATES, "Associates degree (2 year degree)"),
        (BACHELORS, "Bachelors degree (4 year degree)"),
        (MASTERS, "Masters degree"),
        (PHD, "PhD"),
    )

    CATEGORIES = (
        ('HI', 'history'),
        ('MA', 'math'),
        ('SC', 'science'),
        ('LI', 'literature'),
        ('TE', 'technology'),
        ('FI', 'finance'),
        ('MI', 'miscellaneous')
    )

    # Other fields here
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    age = models.IntegerField()
    sex = models.CharField(max_length = 1, choices = SEX_CHOICES)
    country = CountryField()
    education_level = models.CharField(max_length = 200, choices = EDUCATION_CHOICES)
    background_field = models.CharField(max_length = 200)
    first_interest = models.CharField(max_length = 3, choices = CATEGORIES, verbose_name = "First favorite topic:")
    second_interest = models.CharField(max_length = 3, choices = CATEGORIES, verbose_name = "Second favorite topic:")
    desire = models.CharField(max_length = 10000, blank = True, verbose_name = "What are you interested in?")
    
    current_courses = models.ManyToManyField(Course, related_name = "current_users", null = True, blank = True)
    finished_courses = models.ManyToManyField(Course, related_name = "finished_users", null = True, blank = True)
    
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return str(self.user) + "'s Profile"

from django.db.models.signals import post_save

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# post_save.connect(create_user_profile, sender=User)

def get_or_create_user_profile(request):
    profile = None
    user = request.user
    try:
        profile = user.get_profile()
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user = user)
    return profile
"""
class Enrollment(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    curr_night_num = models.IntegerField(null = True, blank = True)
    curr_clip_num = models.IntegerField(null = True, blank = True)

    gold_medal = models.BooleanField()
    silver_medal = models.BooleanField()
    
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    date_completed = models.DateTimeField(null = True, blank = True)
    
    def __unicode__(self):
        return str(self.user) + " taking " + str(self.course)
        """
    