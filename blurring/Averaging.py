import cv2 as cv

img = cv.imread('./Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

cv.waitKey(0)
