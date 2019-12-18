import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to image')
ap.add_argument('-r', '--row', required=True, help = 'row number to display')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
(h, w, num_channels) = image.shape
print 'h=' + str(h) + '; ' + 'w=' + str(w) + '; ' + 'c=' + str(num_channels)

cv2.imshow('Loaded Image', image)
## convert numpy array to list
image_pix = list(image)
## get row and convert each element to Py list
r = int(args['row'])
row = [list(image_pix[r][c]) for c in xrange(w)]
print row
print len(row)
cv2.waitKey(0)

