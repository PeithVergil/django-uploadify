'''
Created on Apr 29, 2012

@author: pvergil
'''

from django.conf import settings

class UploadifyMiddleware(object):
    
    def process_request(self, request):
        if request.method == 'POST' and request.POST.has_key(settings.SESSION_COOKIE_NAME):
            request.COOKIES[settings.SESSION_COOKIE_NAME] = request.POST[settings.SESSION_COOKIE_NAME]