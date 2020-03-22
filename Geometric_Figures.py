import numpy as np
import cv2

#img=cv2.imread('images/lena.jpg',1)       #using imread method
img=np.zeros([512,512,3],np.uint8)     #using np method (Black Screen)

img=cv2.line(img,(0,0),(255,255),(255,0,0),5)       #Line

img=cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),5)   #Arrow Line

img=cv2.rectangle(img,(300,0),(520,180),(0,0,255),-1)  #-1 to fill rectangle

img=cv2.circle(img,(447,63),63,(0,255,0),-1)   #Circle

font=cv2.FONT_HERSHEY_SIMPLEX

img=cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),5,cv2.LINE_AA)

cv2.imshow('image',img)
