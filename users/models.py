from django.db import models
from django.contrib.auth.models import User
from PIL import Image #for resizing profile photos

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #One to one relationship between user and profile
    #cascade deletes both user and profile when user is deleted but deleting profile will not delete user
    #bookmarks = models.ManyToManyField()
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self): #defines how we want the object printed
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path) #Image from pillow library. Image of current instance

        if img.height > 250 or img.width > 250: #if user uploaded profile pic is larger than 250x250 px, resizes to 250x250 px. This is fine for a project of this scope
            output_size = (250,250)
            img.thumbnail(output_size)
            img.save(self.image.path)