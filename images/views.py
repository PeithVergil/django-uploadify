from django.views.generic import ListView

from images.models import Image

class NewPhotos(ListView):
    template_name = 'images/new-photos.html'
    
    def get_queryset(self):
        return Image.objects.filter(owner=self.request.user, stats='N')