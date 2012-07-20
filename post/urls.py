'''
Created on Jul 19, 2012

@author: pvergil
'''

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from post.views import AddView

add = login_required(AddView.as_view())

urlpatterns = patterns('',
    url(r'^add/$', add, name='post_add'),
)