import cv2 as cv 

capture=cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read(0)  ## you can also give file path also 
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
