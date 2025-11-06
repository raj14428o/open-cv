import cv2 as cv

img = cv.imread('./Photos/cats.jpg')
cv.imshow('Cats', img)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

cv.waitKey(0)