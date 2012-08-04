'''
Created on Aug 3, 2012

@author: pvergil
'''

from django import forms

from post.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)