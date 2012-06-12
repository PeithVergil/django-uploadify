'''
Created on Apr 26, 2012

@author: pvergil
'''

import os
import errno

import random
import string

from django.conf import settings
from django.http import HttpResponse
from django.utils import simplejson

ASCII_CHARS = string.ascii_letters + string.digits 

def get_random_string(length=30):
    return ''.join(random.choice(ASCII_CHARS) for x in xrange(length))

def save_upload(data, filename=None):
    mdia_dir = settings.MEDIA_ROOT
    upld_dir = 'uploads'
    
    file_nm, file_ex = os.path.splitext(data.name)
    
    if not filename:
        file_nm = '%s%s' % (get_random_string(), file_ex)
    else:
        file_nm = '%s%s' % (filename, file_ex)
        
    dest_fle = os.path.normpath(os.path.join(mdia_dir, upld_dir, file_nm))
    
    destination = open(dest_fle, 'wb+')
    for chunk in data.chunks():
        destination.write(chunk)
    destination.close()
    
    return dest_fle

def make_directory(directory):
    try:
        os.makedirs(directory)
    except OSError, e:
        if e.errno != errno.EEXIST:
            raise e
        
def jsonResponse(data):
    return HttpResponse(simplejson.dumps(data),
        content_type = 'application/javascript; charset=utf8')