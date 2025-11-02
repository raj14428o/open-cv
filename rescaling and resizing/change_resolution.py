import cv2 as cv # type: ignore

capture=cv.VideoCapture(0)
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,width)

changeRes(720,900)

while True:
    isTrue, frame = capture.read()  ## you can also give file path also
    
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()