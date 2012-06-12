'''
Created on Apr 26, 2012

@author: vergil
'''

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from uploader.views import FileUpload, FileUploadHandler

fileUpload = login_required(FileUpload.as_view())
fileHandler = csrf_exempt(FileUploadHandler.as_view())

urlpatterns = patterns('',
    url(r'^upload/$', fileUpload, name='uploader_fileupload'),
    url(r'^handler/$', fileHandler, name='uploader_filehandler'),
)