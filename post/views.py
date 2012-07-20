from django.views.generic import TemplateView

class AddView(TemplateView):
    template_name = 'post/add.html'