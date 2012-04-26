import os

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView

from uploadify.lib.utils import get_random_string

class FileUpload(TemplateView):
    template_name = 'uploader/file-upload.html'
    
    def post(self, request, *args, **kwargs):
        self._save(request.FILES['Filedata'])
        return HttpResponse()
    
    def _save(self, fdata):
        file_nm, file_ex = os.path.splitext(fdata.name)
        
        file_nm = '%s%s' % (get_random_string(), file_ex)
        
        destination = open(os.path.join(settings.MEDIA_ROOT, 'uploads', file_nm), 'wb+')
        for chunk in fdata.chunks():
            destination.write(chunk)
        destination.close()