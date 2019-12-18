#!/usr/bin/python

import cv2
import sys

##############################################
# module: erosion_dilation.py
# description: erode and dilate images
# @author: vladimir kulyukin
# To run: python erosion_dilation.py <image>
##############################################

img = cv2.imread(sys.argv[1])
cv2.imshow('Original', img)

er_img = cv2.erode(img, (5, 5))
cv2.imshow('Eroded', er_img)

dl_img = cv2.dilate(img, (5, 5))
cv2.imshow('Dilated', dl_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
