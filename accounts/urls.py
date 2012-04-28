'''
Created on Apr 28, 2012

@author: pvergil
'''

from django.conf.urls.defaults import patterns, url

from accounts.views import AccountRegister

#error_messages = {
#    'invalid_login': 'Invalid username or password. Note that both fields are case-sensitive.'
#}

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html'}, name='account_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'accounts/logout.html'}, name='account_logout'),
    url(r'^register/$', AccountRegister.as_view(), name='account_register'),
)