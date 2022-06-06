import cv2
import os
import sys

path = "C:/Users/Weaver/AppData/Roaming/.minecraft/saves/Bad Apple/datapacks/BadApple/data/apple/functions"
count = 0
while(True):
    if os.path.exists(path+"/frames/frame%d.mcfunction"%count):
        if not count % 8 == 0:
            os.remove(path+"/frames/frame%d.mcfunction"%count)
            print("Removed frame %d"%count)
    else:
        if count > 7777:
            break
    count += 1