#!/usr/bin/python

import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

## split the image into 3 channels
B, G, R = cv2.split(image)

## show each channel
print "B's shape:", B.shape
print "G's shape:", G.shape
print "R's shape:", R.shape

cv2.imshow('Red', R)
cv2.imshow('Green', G)
cv2.imshow('Blue', B)

## merge B, G, R channels back to get the original image
merged = cv2.merge([B, G, R])
cv2.imshow('Merged', merged)

amplified_blue = cv2.merge([B+100, G, R])
cv2.imshow('Amplified Blue', amplified_blue)

amplified_green = cv2.merge([B, G+100, R])
cv2.imshow('Amplified Green', amplified_green)

amplified_red = cv2.merge([B, G, R+100])
cv2.imshow('Amplified Red', amplified_red)

cv2.waitKey(0)
cv2.destroyAllWindows()







