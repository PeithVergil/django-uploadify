'''
Created on Jul 2, 2012

@author: pvergil
'''

from django.contrib import admin

from imahe.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)