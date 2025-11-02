import cv2 as cv  # type: ignore
img = cv.imread('./read/Photos/cat.jpg')
cv.imshow('Cat', img)
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)
cv.waitKey(0)