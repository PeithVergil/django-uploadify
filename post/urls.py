'''
Created on Jul 19, 2012

@author: pvergil
'''

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from post.views import AddImage, AddPost, AllPost, AddView, ViewView

_all = AllPost.as_view()
_new = AddPost.as_view()
_img = AddImage.as_view()

_img = csrf_exempt(_img)

_add = login_required(AddView.as_view())
_view = ViewView.as_view()

urlpatterns = patterns('',
    url(r'^$', _all, name='post_all'),
    url(r'^add/$', _add, name='post_add'),
    url(r'^new/$', _new, name='post_new'),
    url(r'^img/$', _img, name='post_img'),
    url(r'^(?P<pid>\d+)/$', _view, name='post_view'),
)