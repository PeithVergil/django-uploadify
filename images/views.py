from django.http import HttpResponseForbidden
from django.views.generic import ListView, View
from django.shortcuts import get_object_or_404

from images.models import Image
from uploadify.lib import imaging, utils

class NewPhotos(ListView):
    template_name = 'images/new-photos.html'
    
    def get_queryset(self):
        images = Image.objects.filter(owner=self.request.user, stats='N')
        return images 
    
class Crop(View):
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        
        id = request.POST.get('id')
        
        x1 = int(float(request.POST.get('x1')))
        y1 = int(float(request.POST.get('y1')))
        x2 = int(float(request.POST.get('x2')))
        y2 = int(float(request.POST.get('y2')))
        
        img = get_object_or_404(Image, id=id)
        
        imaging.crop(img.image.path, (x1, y1, x2, y2))
        imaging.crop(img.thumb.path, (x1, y1, x2, y2))
        
        img.stats = 'C'
        img.save()
        
        return utils.jsonResponse({
            'status': 'OK'
        })