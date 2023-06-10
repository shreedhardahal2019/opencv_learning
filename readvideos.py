import cv2 as cv

video = cv.VideoCapture('C:/Users/shree/opencv_learnings/my_learning/Videos/manang.mp4') #reading the video

while True:                         # grabing the video frame by frame by utilizing video.read() method
    isTrue, frame = video.read()
    cv.imshow('Video', frame)       # display each frame by using imshow() method
    if cv.waitKey(20) & 0xFF==ord('d'):  # to break out of while loop & if the letter 'd' is pressed then break out the loop and stop the video 
        break

video.release() 
cv.destroyAllWindows()