from django.db import models

from django.contrib.auth.models import User

from courses.models import Clip

class Note(models.Model):
    user = models.ForeignKey(User)
    clip = models.ForeignKey(Clip)
    text = models.TextField()
    
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return str(self.user) + " - " + str(self.clip) + ": " + self.text