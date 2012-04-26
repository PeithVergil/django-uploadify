import os

from django.http import HttpResponse
from django.views.generic import TemplateView

from uploadify.lib.utils import get_random_string, save_upload

class FileUpload(TemplateView):
    template_name = 'uploader/file-upload.html'
    
    def post(self, request, *args, **kwargs):
        path = save_upload(request.FILES['Filedata'])
        print 'UPLOADED FILE: %s' % path
        return HttpResponse()