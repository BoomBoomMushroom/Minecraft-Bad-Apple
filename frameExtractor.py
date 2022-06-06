import cv2
import os
import sys

framesFolder = "./frames"
videoFile = "./BadApple.mp4"
size = (1/24, 1/24) # was 1920 x 1080
resize = True

vidcap = cv2.VideoCapture(videoFile)
success, image = vidcap.read()
count = 0
while(success):
    if resize:
        image = cv2.resize(image,(0,0),fx=size[0],fy=size[1])
    cv2.imwrite(framesFolder+"/frame%d.png" % count, image)
    
    success2, image = vidcap.read()
    count += 1
    print( "Loading new frame " + str(count) + ": " + str(success2) )
    if not success2:
        print("Done!")
        break