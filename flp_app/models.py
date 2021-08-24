from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    favorite = models.ManyToManyField(User, related_name='blog_posts')
    #author = models.ForeignKey(User, on_delete=models.CASCADE) user is author, if user is deleted, deletes their posts as well

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk}) 
    # ^^^this redirects to an instance of a blog post when a blog post is created

class Bookmark(models.Model):
    posts = models.ManyToManyField(Post)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmark_post')