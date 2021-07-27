import os
import cv2
import math
from PIL import Image
import matplotlib.pyplot as plt
import glob
import numpy as np

"""
#Question 1
vidcap = cv2.VideoCapture("C:/Users/sirap/Desktop/dogCat/chicken_run.mp4")
fps  =  vidcap.get(cv2.CAP_PROP_FPS)
count = 1


while vidcap.isOpened():
    
    frame_num =  vidcap.get(cv2.CAP_PROP_POS_FRAMES)
    success, frame = vidcap.read()
    
    if (success != True):
        print("Error")
        break
    
    if (frame_num % math.floor(fps/2) == 0) :
        cv2.imwrite(os.path.join("C:/Users/sirap/Desktop/dogCat/chicky",
        "frame_"+ str(int(count)) + ".png"), frame)
        count += 1   

   
cv2.destroyAllWindows()
vidcap.release()
#print("Finish!")
"""

"""
#Question 2
path = "C:/Users/sirap/Desktop/dogCat/chicky"
list_item = os.listdir(path)
print("There are ",len(list_item)," items in folder")
#print(list_item)
png = []

def classify():
    for i in list_item:
        #print(i)
        y = i.split(".png")
        z = y[0] 
        png.append(z)  
    print("PNG format of this folder is",png)

classify()
"""

#Question 3

file_list = glob.glob("C:/Users/sirap/Desktop/dogCat/chicky/*.*")

def createGray():
    count = 0
    for picture in file_list:
        gray = cv2.imread(picture,0)
        cv2.imwrite(os.path.join("C:/Users/sirap/Desktop/dogCat/gray" , "gray_"+ str(int(count)) + ".png"), gray)
        count += 1

gray_list = glob.glob("C:/Users/sirap/Desktop/dogCat/gray/*.*")
array = []

def countBrightness():
    for gray in gray_list  : 
        img = cv2.imread(gray)
        #print(img)
        #print("Sum  = ",cv2.sumElems(img))
        Sum = cv2.sumElems(img)[0]
        #print("Size = ",img.size)
        bright = Sum/img.size
        #print("Brightness = ",Sum/img.size)
        array.append(bright)
        
countBrightness()

plt.plot(array)
plt.ylabel("Brightness Level")
plt.xlabel("Frame Number")
plt.show()











