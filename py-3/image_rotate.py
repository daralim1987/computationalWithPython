import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-ip', '--img_path', required = True, help = 'path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['img_path'])
# height, width, num of channels
(h, w, nc) = image.shape
img_center = (w / 2, h / 2)

# rotate the image around the center by +180 degrees
RM180 = cv2.getRotationMatrix2D(img_center, 180, 1.0)
rotated_image180 = cv2.warpAffine(image, RM180, (w, h))

# rotate the image around the center by +90 degrees
RM90 = cv2.getRotationMatrix2D(img_center, 90, 1.0)
rotated_image90 = cv2.warpAffine(image, RM90, (w, h))

# rotate the image around the center by -90 degrees
RMmin90 = cv2.getRotationMatrix2D(img_center, -90, 1.0)
rotated_image_min90 = cv2.warpAffine(image, RMmin90, (w, h))

# rotate the image around the center by +45 degrees
RM45 = cv2.getRotationMatrix2D(img_center, 45, 1.0)
rotated_image45 = cv2.warpAffine(image, RM45, (w, h))

# rotate the image around the center by -45 degrees
RMmin45 = cv2.getRotationMatrix2D(img_center, -45, 1.0)
rotated_image_min45 = cv2.warpAffine(image, RMmin45, (w, h))

cv2.imshow('Original Image', image)
cv2.imshow('Rotated by  +180', rotated_image180)
cv2.imshow('Rotated by  +90', rotated_image90)
cv2.imshow('Rotated by  -90', rotated_image_min90)
cv2.imshow('Rotated by  +45', rotated_image45)
cv2.imshow('Rotated by  -45', rotated_image_min45)

cv2.waitKey(0)

cv2.destroyAllWindows()
