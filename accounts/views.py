from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView

from accounts.forms import RegistrationForm

class AccountRegister(TemplateView):
    template_name = 'accounts/register.html'
    
    def get_context_data(self, **kwargs):
        form = RegistrationForm()
        return {
            'form': form
        }
        
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            usrnm = form.cleaned_data.get('usrnm')
            email = form.cleaned_data.get('email')
            passw = form.cleaned_data.get('pass1')
            
            user = User.objects.create_user(usrnm, email, passw)
            user.first_name = fname
            user.last_name  = lname
            
            user.save()
            
            return redirect('account_login')
        else:
            return self.render_to_response({
                'form': form
            })