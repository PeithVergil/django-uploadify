from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, TemplateView
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect

from imahe.forms import PhotoEditorForm
from imahe.models import Photo
from uploadify.lib import imaging, utils

class Gallery(ListView):
    template_name = 'imahe/gallery.html'
    
    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user) 

class Upload(TemplateView):
    template_name = 'imahe/upload.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['session_nm'] = settings.SESSION_COOKIE_NAME
        context['session_ky'] = request.session.session_key
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        user = request.user
        
        if user.is_authenticated():
            data = request.FILES['Filedata']
            
            photo = Photo.objects.create(image=data, thumb=data, owner=user)
            # Resize the thumbnail to 180x180 pixels
            imaging.fit(photo.thumb.path)
            
            return utils.jsonResponse({
                'redirect': reverse('imahe_editor', args=[photo.id]),
                'message': 'Photo uploaded',
                'status': 'OK'
            })
        else:
            return HttpResponseForbidden()
        
class Crop(TemplateView):
    template_name = 'imahe/crop.html'
    
    def post(self, request, *args, **kwargs):
        user = request.user
        
        if user.is_authenticated():
            id = request.POST.get('id')
            
            x1 = int(float(request.POST.get('x1')))
            y1 = int(float(request.POST.get('y1')))
            x2 = int(float(request.POST.get('x2')))
            y2 = int(float(request.POST.get('y2')))
            
            img = get_object_or_404(Photo, id=id)
            
            imaging.crop(img.image.path, (x1, y1, x2, y2))
            imaging.crop(img.thumb.path, (x1, y1, x2, y2))
            
            img.stats = 'C'
            img.save()
            
            return utils.jsonResponse({
                'status': 'OK'
            })
        else:
            return HttpResponseForbidden()
        
class ImageViewer(DetailView):
    template_name = 'imahe/viewer.html'
    context_object_name = 'photo'
    model = Photo

class ImageEditor(TemplateView):
    template_name = 'imahe/editor.html'
    
    def get_context_data(self, **kwargs):
        photo = get_object_or_404(Photo, pk = kwargs.get('pk'))
        form = PhotoEditorForm(instance=photo)
        return {
            'photo': photo,
            'form': form
        }
        
    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        form = PhotoEditorForm(request.POST, instance=photo)
        
        if form.is_valid():
            title = form.cleaned_data.get('title')
            descr = form.cleaned_data.get('description')
            
            photo.description = descr
            photo.title = title
            photo.save()
            
            return redirect(
                'imahe_viewer',
                kwargs.get('pk')
            )
            
        return self.render_to_response({
            'photo': photo,
            'form': form
        })