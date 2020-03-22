#This programs connects last two points and points are formed by left click event
import cv2
import numpy as np

events=[i for i in dir(cv2) if 'EVENT' in i ]    #dir is a default inbuilt method which shows all the classes and member functions inside cv2 package
print(events)     #prints all the mouse events inside cv2

#creating mouse call back function

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorImage=np.zeros((512,512,3),np.uint8)

        mycolorImage[:]=[blue,green,red]
        cv2.imshow('ColorWindow',mycolorImage)
        
#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('images/lena.jpg')
cv2.imshow('Name of Window',img)
points=[]
cv2.setMouseCallback('Name of Window',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()


