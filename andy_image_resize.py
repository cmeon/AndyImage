#!/usr/bin/env python

import sys
from os import path, mkdir
from vipsCC import *

sizes = { 'ldpi':3, 'mdpi':4, 'hdpi':6, 'xhdpi':8, 'xxhdpi':12, 'xxxhdpi':16 }

if ( len(sys.argv) < 2):
    print """
  (H)Andy Image Resize
  -----------------------------------
  This program resizes images into ldpi to xxxhdpi
  ** It uses xxhdpi as the base image size and not hdpi like in the Android docs.

  usage: andy_image_resize.py <image> [<folder>]
         <image>  - filename of the image file with extension.
         <folder> - may be the path to resource folder of an Android app project.
"""
    exit(1)

try:
    fullname = sys.argv[1]
    basename = path.basename(sys.argv[1])
    filename, extension = tuple(path.splitext(basename))
    image = VImage.VImage(fullname)
    basefolder = '.'

    try:
        basefolder = sys.argv[2]
    except IndexError, e:
        print 'Printing on current folder'

    for k, v in sizes.items():
        red = float(16/v)
        folder = basefolder+'/'+'drawable-'+k
        try:
            mkdir(folder)
        except OSError, e:
            image.shrink(red, red).write(folder +'/'+ filename+extension)
        else:
            image.shrink(red, red).write(folder +'/'+ filename+extension)

except VError.VError, e:
    e.perror(sys.argv[0])

