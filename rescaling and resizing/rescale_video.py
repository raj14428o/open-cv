import cv2 as cv # type: ignore

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1] * scale)
    length= int(frame.shape[0] * scale)
    dimensions = (width,length)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)


capture=cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read(0)  ## you can also give file path also
    frame_resized= rescaleFrame(frame)
    cv.imshow('Video',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
