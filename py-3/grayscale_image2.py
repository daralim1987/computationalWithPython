#!/usr/bin/python

import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'], 0) ## this actually reads an image and
                                     ## converts it to grayscale
cv2.imshow('Grayscaled', image)
cv2.waitKey()

cv2.destroyAllWindows()



