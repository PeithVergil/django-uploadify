'''
Created on Apr 28, 2012

@author: pvergil
'''

from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    fname = forms.CharField(label = 'First Name')
    lname = forms.CharField(label = 'Last Name')
    usrnm = forms.CharField(label = 'Username')
    email = forms.EmailField(label = 'Email', required=False)
    pass1 = forms.CharField(widget = forms.PasswordInput, label = 'Password')
    pass2 = forms.CharField(widget = forms.PasswordInput, label = 'Password Confirmation')
    
    def clean_pass2(self):
        p1 = self.cleaned_data.get('pass1', '')
        p2 = self.cleaned_data.get('pass2', '')
        
        if p1 != p2:
            raise forms.ValidationError('The password and password confirmation did not match')
        
        return p2