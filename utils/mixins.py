'''
Created on Aug 3, 2012

@author: pvergil
'''

import json

from django.http import HttpResponse

class JSONResponseMixin(object):
    response = HttpResponse

    def render_to_response(self, context, **kwargs):
        kwargs['content_type'] = 'application/javascript; charset=utf8'

        return self.response(
            self.to_json(context), **kwargs
        )

    def to_json(self, context):
        return json.dumps(context)