import os
import cv2
import math
from PIL import Image
import matplotlib.pyplot as plt
import glob

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
        cv2.imwrite(os.path.join("C:/Users/sirap/Desktop/dogCat/chicky", "frame_"+ str(int(count)) + ".png"), frame)
        count += 1   
   



cv2.destroyAllWindows()
vidcap.release()
#print("Finish!")
"""

"""
#Question 2
arr = os.listdir("C:/Users/sirap/Desktop/dogCat/chicky")
print(len(arr))
print(arr)
"""

#Question 3

file_list = glob.glob("C:/Users/sirap/Desktop/dogCat/chicky/*.*")

count = 0
for picture in file_list:
    gray = cv2.imread(picture,0)
    cv2.imwrite(os.path.join("C:/Users/sirap/Desktop/dogCat/gray" , "gray_"+ str(int(count)) + ".png"), gray)
    count += 1











