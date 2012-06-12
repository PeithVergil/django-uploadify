'''
Created on Jun 11, 2012

@author: pvergil
'''

from django import forms

class PhotoEditForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Photo title'}))
    descr = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder': 'Photo Description'}))