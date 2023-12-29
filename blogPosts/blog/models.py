from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#users to post is a one to many relationship
#Create post model
class Post(models.Model):
    #title field will be a char field with max length 100
    title = models.CharField(max_length = 100)
    #Textfield is same as charfield but with unrestricted amount of text
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    #Use foreign key for one to many post author relationship
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    #Magic methods or special methods 
    def __str__(self):
        return self.title