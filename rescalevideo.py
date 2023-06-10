import cv2 as cv

def rescaleFrame(frame, scale=0.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading video

video = cv.VideoCapture('C:/Users/shree/opencv_learnings/my_learning/Videos/manang.mp4') #reading the video

while True:                         # grabing the video frame by frame by utilizing video.read() method
    isTrue, frame = video.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)       # display each frame by using imshow() method

    cv.imshow('Resized Video', frame_resized)


    if cv.waitKey(20) & 0xFF==ord('d'):  # to break out of while loop & if the letter 'd' is pressed then break out the loop and stop the video 
        break

video.release() 
cv.destroyAllWindows()