'''
Created on Aug 1, 2012

@author: pvergil
'''

from django import template

register = template.Library()

@register.inclusion_tag('imahe/uploadify_dependencies.html')
def uploadify_dependencies():
    return {}

@register.inclusion_tag('imahe/uploadify_button.html')
def uploadify_button():
    return {}