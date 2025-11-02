import cv2 as cv # type: ignore

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)