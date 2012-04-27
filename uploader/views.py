from django.http import HttpResponse
from django.views.generic import TemplateView

from images.models import Image

class FileUpload(TemplateView):
    template_name = 'uploader/file-upload.html'
    
    def post(self, request, *args, **kwargs):
        data = request.FILES['Filedata']
        
        image = Image(image = data)
        image.save()
        
        return HttpResponse()