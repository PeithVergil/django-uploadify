import os

from django.contrib.auth.models import User
from django.db import models
from django.utils.dateformat import format

from uploadify.lib.utils import get_random_string

def image_upload(instance, filename):
    file_nm, file_ex = os.path.splitext(filename)
    return 'uploads/%d/%s%s' % (instance.owner.id, get_random_string(), file_ex)

class Image(models.Model):
    owner = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=image_upload)
