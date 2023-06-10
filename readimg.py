import cv2 as cv

img = cv.imread('C:/Users/shree/opencv_learnings/my_learning/Images/flower.jpg') # reading the image

cv.imshow('Flower', img) # displaying the image

cv.waitKey(0) # waits for infinity amount of time key to be pressed