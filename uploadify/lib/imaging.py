'''
Created on May 15, 2012

@author: pvergil
'''

import Image
import ImageOps

def fit(path, size=(180, 180)):
    img = Image.open(path)
    fit = ImageOps.fit(img, size, Image.ANTIALIAS)
    fit.save(path)

def crop(path, box=(0, 0, 450,450)):
    img = Image.open(path)
    crp = img.crop(box)
    crp.save(path)
    
def resize(path, size=(450,450)):
    img = Image.open(path)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(path)