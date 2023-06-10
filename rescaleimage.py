import cv2 as cv

img = cv.imread('C:/Users/shree/opencv_learnings/my_learning/Images/flower.jpg')

cv.imshow('Flower', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Resized Image', resized_image)

cv.waitKey(0)