import os
import datetime

from django.contrib.auth.models import User
from django.db import models

import utils

def image_upload(instance, filename):
    return _upload(instance, filename, 'uploads/%d/images/%d/%d/%d/%s%s')

def thumb_upload(instance, filename):
    return _upload(instance, filename, 'uploads/%d/thumbs/%d/%d/%d/%s%s')

def _upload(instance, filename, path):
    today = datetime.datetime.now()
    file_nm, file_ex = os.path.splitext(filename)
    return path % (instance.post.author.id, today.year, today.month, today.day, utils.get_random_string(), file_ex)

class Post(models.Model):
    author = models.ForeignKey(User)
    content = models.CharField(max_length=255)
    postdate = models.DateTimeField(auto_now_add=True)
    
    @models.permalink
    def get_absolute_url(self):
        return ('post_view', (self.id,))
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='postimages')
    
    image = models.ImageField(upload_to=image_upload)
    thumb = models.ImageField(upload_to=thumb_upload)
    
    def get_absolute_url(self):
        return ('post_image', (self.id,))