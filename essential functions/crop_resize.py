
import cv2 as cv # type: ignore

# Read in an image
img = cv.imread('./read/Photos/cat.jpg')
cv.imshow('Cat', img)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)