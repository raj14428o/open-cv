import cv2 as cv  # type: ignore
img = cv.imread('./read/Photos/cat.jpg')
cv.imshow('Cat', img)
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)
# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

cv.waitKey(0)