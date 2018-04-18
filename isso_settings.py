#!/usr/bin/env python

from sys import argv
from os import environ
from glob import glob

# settings = environ.get('ISSO_SETTINGS')
settings = argv[1]

if '*' in settings:
    print(';'.join(glob(settings)))
else:
    print(settings)
