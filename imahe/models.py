import os
import datetime

from django.contrib.auth.models import User
from django.db import models

from uploadify.lib.utils import get_random_string

def image_upload(instance, filename):
    return _upload(instance, filename, 'uploads/%d/images/%d/%d/%d/%s%s')

def thumb_upload(instance, filename):
    return _upload(instance, filename, 'uploads/%d/thumbs/%d/%d/%d/%s%s')

def _upload(instance, filename, path):
    today = datetime.datetime.now()
    file_nm, file_ex = os.path.splitext(filename)
    return path % (instance.owner.id, today.year, today.month, today.day, get_random_string(), file_ex)

STATUS_CHOICES = (
    ('N', 'New'),
    ('C', 'Cropped'),
)

class Photo(models.Model):
    owner = models.ForeignKey(User)
    image = models.ImageField(upload_to=image_upload)
    thumb = models.ImageField(upload_to=thumb_upload)
    title = models.CharField(max_length=160, default='Untitled')
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    date = models.DateTimeField(auto_now_add=True)

class Imahe(models.Model):
    owner = models.ForeignKey(User)
    image = models.ImageField(upload_to=image_upload)
    thumb = models.ImageField(upload_to=thumb_upload)
    stats = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    date  = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    desc  = models.CharField(max_length=255, blank=True, null=True)
