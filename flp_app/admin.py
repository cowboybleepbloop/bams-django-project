from django.contrib import admin
from .models import Bookmark, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Bookmark)

