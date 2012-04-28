from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import View, TemplateView

from images.models import Image

class FileUpload(TemplateView):
    template_name = 'uploader/file-upload.html'
    
    def get(self, request, *args, **kwargs):
        context = {
            'session_nm': settings.SESSION_COOKIE_NAME,
            'session_ky': request.session.session_key
        }
        return self.render_to_response(context)
    
class FileUploadHandler(View):
    
    def post(self, request, *args, **kwargs):
        user = request.user
        
        if user.is_authenticated():
            data = request.FILES['Filedata']
            
            image = Image(image = data, owner = user)
            image.save()
            
            return HttpResponse()
        else:
            return HttpResponseForbidden()