#/usr/bin/python

import cv2
import argparse

################################################
# module: bgr_to_hsv.py
# author: vladimir kulyukin
# description: convert an input image into HSV,
# get access to individual pixels and
# channels.
################################################

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

## if you want to filter on color, filter on Hue.
## Hue - color value [0 - 179].
## Saturation - vibrancy of color [0, 255]; at lower saturation everyhthing is
## White in the center of the cylinder; at high saturation, you are starting to
## get rich colors;
## Value - brightness or intensity [0, 255]; value goes from dark (below)
## to bright (above)
## These are good Hue ranges:
## READ     - [165, 5]
## GREEN    - [45, 75]
## BLUE     - [90, 120]

image = cv2.imread(args['image'])
#print image

print 'original shape:', image.shape
orig_pix = image[10, 50]
print 'orig_pix at 10, 50:', orig_pix

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print 'gray shape:', gray_image.shape
gray_pix = gray_image[10, 50]
print 'gray_pix at 10, 50:', gray_pix

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print 'hsv_shape:', hsv_image.shape
hsv_pix = hsv_image[10, 50]
print 'hsv_pix at 10, 50:', hsv_pix 

cv2.imshow('Original image', image)
cv2.imshow('HSV image', hsv_image)
cv2.imshow('Hue channel', hsv_image[:, :, 0])
cv2.imshow('Saturation channel', hsv_image[:, :, 1])
cv2.imshow('Value channel', hsv_image[:, :, 2])

cv2.waitKey()
cv2.destroyAllWindows()




