'''
Created on Aug 5, 2012

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
    
def resize(path, size=(620,620)):
    img = Image.open(path)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(path)
    
def resizeWidth(path, width=620):
    img = Image.open(path)
    
    maxw = width
    
    # Calculate ratio
    rtio = float(maxw) / img.size[0]
    # Calculate max height
    maxh = int(rtio * img.size[1])
    
    img.resize((maxw, maxh), Image.ANTIALIAS).save(path)