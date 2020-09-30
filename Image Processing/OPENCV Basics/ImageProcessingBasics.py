# OpenCV Tutorial
# Tutorial from PyImageSearch

import argparse
import cv2
import imutils

# Argument parser definition
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

# load the input image and show its dimensions
image = cv2.imread(args["image"])

# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
cv2.imshow("Image", image)
cv2.waitKey(0)

# Access BGR pixel x=50,y=100
# BGR rather than RGB, pixels [y,x]
(B,G,R) = image[100,50]
print("R={}, G={}, B={}".format(R,G,B))

# ROI (Region of Interest)
# Rectangle from x,y = 320,60 to x,y = 420,160
rx,ry,rw,rh = cv2.selectROI("Image", image)
#roi = img[220:420, 160:360]
roi = image[ry:ry+rh, rx:rx+rw]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)

# imutils library 
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)