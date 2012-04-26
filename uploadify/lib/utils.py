'''
Created on Apr 26, 2012

@author: vergil
'''

import random
import string

ASCII_CHARS = string.ascii_letters + string.digits 

def get_random_string(length=30):
    return ''.join(random.choice(ASCII_CHARS) for x in xrange(length))