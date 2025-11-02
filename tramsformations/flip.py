import cv2 as cv

# Load the image
img = cv.imread('./photos/park.jpg')

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Flip both vertically and horizontally
    flip = cv.flip(img, -1)
    cv.imshow('Flip both vertically and horizontally', flip)

    # Flip horizontally
    flip1 = cv.flip(img, 1)
    cv.imshow('Flip horizontally', flip1)

    # Flip vertically
    flip2 = cv.flip(img, 0)
    cv.imshow('Flip vertically', flip2)

    # Wait for a key press and close all windows
    cv.waitKey(0)
    cv.destroyAllWindows()