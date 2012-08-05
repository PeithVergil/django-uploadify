from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic import DetailView, TemplateView, View

from post.forms import PostForm
from post.models import Post, PostImage
from utils.mixins import JSONResponseMixin
from utils import imaging

class AddView(TemplateView):
    template_name = 'post/add.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        context['session_nm'] = settings.SESSION_COOKIE_NAME
        context['session_ky'] = request.session.session_key
        
        context['postform'] = PostForm()
        context['user'] = request.user
        
        return self.render_to_response(context)
    
class AllPost(TemplateView):
    template_name = 'post/all.html'
    
    def get(self, request, *args, **kwargs):
        context = {
            'user': request.user,
            'postform': PostForm()
        }
        
        if request.user.is_authenticated():
            return self._a(request, context, *args, **kwargs)
        else:
            return self._b(request, context, *args, **kwargs)
    
    def _a(self, request, context, *args, **kwargs):
        context['posts'] = Post.objects.filter(author = request.user).order_by('-postdate')
        return self.render_to_response(context)
    
    def _b(self, request, context, *args, **kwargs):
        context['posts'] = Post.objects.all().order_by('-postdate')
        return self.render_to_response(context)
    
class AddPost(JSONResponseMixin, View):
    def post(self, request, *args, **kwargs):        
        content = request.POST.get('content')
        userid = request.POST.get('userid')
        
        context = { 'status': 0 }
        try:
            user = User.objects.get(id=userid)
            
            if user == request.user:
                post = Post.objects.create(author=user, content=content)
                
                context['message'] = 'New post added.'
                context['postid']  = post.id
                context['status']  = 1
            else:
                context['message'] = 'Invalid user ID.'
        except User.DoesNotExist:
            context['message'] = 'User does not exist.'
        
        return self.render_to_response(context)

class AddImage(JSONResponseMixin, View):
    def post(self, request, *args, **kwargs):
        postid = request.POST.get('postid')
        
        context = { 'status': 0 }
        try:
            data = request.FILES['Filedata']
            
            post = Post.objects.get(id=postid)
            
            image = PostImage.objects.create(post=post, image=data, thumb=data)
            
            # Resize the photo so it has a width of 620 pixels
            imaging.resizeWidth(image.image.path)
            # Resize the thumbnail to 80x80 pixels
            imaging.resizeThumb(image.thumb.path)
            
            context['message'] = 'New image added.'
            context['imageid'] = image.id
            context['status']  = 1
        except Post.DoesNotExist:
            context['message'] = 'Post does not exist.'
        
        return self.render_to_response(context)
    
class ViewView(DetailView):
    model = Post