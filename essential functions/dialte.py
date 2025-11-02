import cv2 as cv  # type: ignore
img = cv.imread('./read/Photos/cat.jpg')
cv.imshow('Cat', img)
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)
# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)
cv.waitKey(0)