import cv2 as cv
import numpy as np

img = cv.imread('./photos/park.jpg')


# rotate around center
def rotate(img,angle, rotPoint=None): 
    (height,width) = img.shape[:2] 
    if rotPoint == None:
        rotPoint = (height//2 , width//2)
    rotMat= cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimension = (width,height)

    return cv.warpAffine(img,rotMat,dimension)

rotated = rotate(img,45)
cv.imshow('Park',img)
cv.imshow('Rotated',rotated)
cv.waitKey(0)