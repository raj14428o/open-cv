import cv2 as cv

img = cv.imread('./Photos/cats.jpg')
cv.imshow('Cats', img)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)