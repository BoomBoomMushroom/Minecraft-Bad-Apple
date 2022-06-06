import os
import sys
import cv2
import numpy as np
import json

path = "C:/Users/Weaver/AppData/Roaming/.minecraft/saves/Bad Apple/datapacks/BadApple/data/apple/functions"
frame = 0

def allValue(array,value):
    for item in array:
        if item != value:
            return False
    return True
def writeFile(frame):
    funct = open(path+"/frames/frame%d.mcfunction"%frame, "w")
    image = cv2.imread("./frames/frame%d.png"%frame)
    rows,cols,_ = image.shape
    for x in range(rows):
        for y in range(cols):
            pixil = image[x,y]
            totalPixil = int(pixil[0])+int(pixil[1])+int(pixil[2])
            isWhite = totalPixil > 382
            cmd = "setblock " + str(x) + " -60 " + str(y)
            if isWhite:
                cmd += " iron_block"
            else:
                cmd += " coal_block"
            funct.write(cmd+"\n")

while True:
    if not frame % 8:
        writeFile(frame)
        print("Frame %d done!"%frame)
    frame += 1