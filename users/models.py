from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    age = models.IntegerField()
    sex = models.CharField(max_length = 1)
    country = models.CharField(max_length = 200)
    education_level = models.CharField(max_length = 200)
    background_field = models.CharField(max_length = 200)
    desire = models.CharField(max_length = 10000)

from django.db.models.signals import post_save

# definition of UserProfile from above
# ...

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)