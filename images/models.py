import os

from django.contrib.auth.models import User
from django.db import models
from django.utils.dateformat import format

from uploadify.lib.utils import get_random_string

def image_upload(instance, filename):
    return _upload(instance, filename, 'uploads/%d/image/%s%s')

def thumb_upload(instance, filename):
    return _upload(instance, filename, 'uploads/%d/thumb/%s%s')

def _upload(instance, filename, path):
    file_nm, file_ex = os.path.splitext(filename)
    return path % (instance.owner.id, get_random_string(), file_ex)

STATUS_CHOICES = (
    ('N', 'New'),
    ('C', 'Cropped'),
)

class Image(models.Model):
    owner = models.ForeignKey(User)
    image = models.ImageField(upload_to=image_upload)
    thumb = models.ImageField(upload_to=thumb_upload)
    stats = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    date  = models.DateTimeField(auto_now_add=True)
