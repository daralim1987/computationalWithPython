import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to image')
ap.add_argument('-c', '--col', required=True, help = 'col number to display')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
(h, w, num_channels) = image.shape
print 'h=' + str(h) + '; ' + 'w=' + str(w) + '; ' + 'c=' + str(num_channels)

cv2.imshow('Loaded Image', image)
## convert numpy array to list
image_pix = list(image)
c = int(args['col'])
col = [tuple(image_pix[r][c]) for r in xrange(h)]
same_col = image[:,c]
for i in xrange(len(col)):
    assert col[i] ==  tuple(same_col[i])
print same_col
cv2.waitKey(0)

