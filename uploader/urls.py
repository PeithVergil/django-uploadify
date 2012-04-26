'''
Created on Apr 26, 2012

@author: vergil
'''

from django.conf.urls.defaults import patterns, url
from django.views.decorators.csrf import csrf_exempt

from uploader.views import FileUpload

fileupload_view = csrf_exempt(FileUpload.as_view())

urlpatterns = patterns('',
    url(r'^upload/$', fileupload_view, name='uploader_fileupload'),
)