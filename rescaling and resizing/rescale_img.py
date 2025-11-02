import cv2 as cv # type: ignore

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1] * scale)
    length= int(frame.shape[0] * scale)
    dimensions = (width,length)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
cv.waitKey(0)