from django.db import models
from django.contrib.auth.models import User
# django gives user models, database for particular user
# User model takes care of user info like username email , password
# Create your models here. - similar to database

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)        #if user deleted all child tasks are deleted(CASCADE) or items to remain(SET_NULL) 
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)      # auto date time stamp

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']         #order by complete status
        
