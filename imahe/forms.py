'''
Created on Jun 11, 2012

@author: pvergil
'''

from django import forms

from imahe.models import Photo

class PhotoEditorForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Photo title'}),
                            error_messages={'required': 'Please enter a title for this photo.'})
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder': 'Photo Description'}),
                            required=False)
    
    class Meta:
        model = Photo
        fields = ('title', 'description',)