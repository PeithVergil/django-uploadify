'''
Created on May 21, 2012

@author: pvergil
'''

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from imahe.views import Gallery, ImageEditor, ImageViewer, Upload, Crop

gallery = login_required(Gallery.as_view())
upload = login_required(Upload.as_view())
crop = login_required(Crop.as_view())

viewer = login_required(ImageViewer.as_view())
editor = login_required(ImageEditor.as_view())

upload = csrf_exempt(upload)

urlpatterns = patterns('',
    url(r'^gallery/$', gallery, name='imahe_gallery'),
    url(r'^upload/$', upload, name='imahe_upload'),
    url(r'^crop/$', crop, name='imahe_crop'),
    
    url(r'^view/(?P<pk>\d+)/$', viewer, name='imahe_viewer'),
    url(r'^edit/(?P<pk>\d+)/$', editor, name='imahe_editor'),
)