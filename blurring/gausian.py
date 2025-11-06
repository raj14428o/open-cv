import cv2 as cv

img = cv.imread('./Photos/cats.jpg')
cv.imshow('Cats', img)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

cv.waitKey(0)
