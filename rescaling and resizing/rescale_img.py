import cv2 as cv

img = cv.imread('./photos/cat.jpg')
cv.imshow('Original Cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

rescaled_img = rescaleFrame(img)
cv.imshow('Rescaled Cat', rescaled_img)

cv.waitKey(0)
cv.destroyAllWindows()