import os
import sys
import cv2

path = "C:/Users/Weaver/AppData/Roaming/.minecraft/saves/Bad Apple/datapacks/BadApple/data/apple/functions"

def writeFile():
    f = open(path+"/render.mcfunction","w")
    d = ""
    p1 = "execute if score f frame matches "
    p2 = " run function apple:frames/"
    for filename in os.listdir(path+"/frames"):
        d += p1 + filename.split(".")[0].split("frame")[1] + p2 + filename.split(".")[0]+"\n"
    f.write(d)
writeFile()