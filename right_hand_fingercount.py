import cv2
import time
import os
#importing handDetector from image
import image as htm

wCam, hCam=1000,500

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

folderPath="FingerImages"
myList=os.listdir(folderPath)
print(myList)
overlayList=[]
for imPath in myList:
    image=cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
    print(len(overlayList))
