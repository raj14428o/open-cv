import cv2 as cv
import numpy as np

# Load image
img = cv.imread('./Photos/cats 2.jpg')
cv.imshow('Original Image', img)

# Create blank mask
blank = np.zeros(img.shape[:2], dtype='uint8')

# Circle mask
circle_mask = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle Mask', circle_mask)

# Rectangle mask
rectangle_mask = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv.imshow('Rectangle Mask', rectangle_mask)

# Combined mask (intersection of circle and rectangle)
weird_shape = cv.bitwise_and(circle_mask, rectangle_mask)
cv.imshow('Weird Shape Mask', weird_shape)

# Apply masks
masked_circle = cv.bitwise_and(img, img, mask=circle_mask)
cv.imshow('Circle Masked Image', masked_circle)

masked_rectangle = cv.bitwise_and(img, img, mask=rectangle_mask)
cv.imshow('Rectangle Masked Image', masked_rectangle)

masked_weird = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked_weird)

cv.waitKey(0)
cv.destroyAllWindows()