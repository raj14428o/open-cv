import cv2 as cv  # type: ignore
img = cv.imread('./read/Photos/cat.jpg')
cv.imshow('Cat', img)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
cv.waitKey(0)