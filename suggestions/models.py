from django.db import models

from django.contrib.auth.models import User

class Suggestion(models.Model):
    user = models.ForeignKey(User, null = True, blank = True)
    suggestion = models.TextField()
    
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        if self.user is None:
            return "Anonymous: " + self.suggestion
        else:
            return str(self.user) + ": " + self.suggestion