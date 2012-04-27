import os

from django.db import models
from django.utils.dateformat import format

from uploadify.lib.utils import get_random_string

def image_upload(instance, filename):
    file_nm, file_ex = os.path.splitext(filename)
    return 'uploads/%s/%s%s' % (format(instance.date, u'U'), get_random_string(), file_ex)

class Image(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=image_upload)
