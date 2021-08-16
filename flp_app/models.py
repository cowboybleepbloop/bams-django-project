from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    content = models.TextField() #can we use something else to allow html within the content body?
    date_posted = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE) user is author, if user is deleted, deletes their posts as well

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk}) 
    # ^^^this redirects to an instance of a blog post when a blog post is created

class Comment(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #user is author, if user is deleted, deletes their posts as well
    content = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now)
   

    def __str__(self):
        return self.title
