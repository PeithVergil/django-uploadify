'''
Created on May 9, 2012

@author: pvergil
'''

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from images.views import NewPhotos

newPhotos = login_required(NewPhotos.as_view())

urlpatterns = patterns('',
    url(r'^new-photos/$', newPhotos, name='images_newphotos'),
)