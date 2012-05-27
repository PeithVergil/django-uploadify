'''
Created on May 9, 2012

@author: pvergil
'''

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from images.views import NewPhotos, Crop

newPhotos = login_required(NewPhotos.as_view())
crop = login_required(Crop.as_view())

urlpatterns = patterns('',
    url(r'^new-photos/$', newPhotos, name='images_newphotos'),
    url(r'^crop/$', crop, name='images_crop'),
)