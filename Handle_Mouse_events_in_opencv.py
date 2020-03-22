import cv2
import numpy as np

events=[i for i in dir(cv2) if 'EVENT' in i ]    #dir is a default inbuilt method which shows all the classes and member functions inside cv2 package
print(events)     #prints all the mouse events inside cv2

#creating mouse call back function

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,' ,',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY=str(x)+','+str(y)                                  #left click event (Prints x andy coordinates)
        cv2.putText(img,strXY,(x,y),font,1,(255,255,0),5)
        cv2.imshow('Name of Window',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        print(x,' ,',y)                                                         #Right click event (Prints RGB Values of particular coordinates)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strBGR=str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,strBGR,(x,y),font,1,(0,255,255),5)
        cv2.imshow('Name of Window',img)

#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('images/lena.jpg')
cv2.imshow('Name of Window',img)

cv2.setMouseCallback('Name of Window',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()


