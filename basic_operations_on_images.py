import numpy as np
import cv2

img=cv2.imread('images/messi5.jpg')
img2=cv2.imread('images/opencv-logo.png')    #for add images 2nd pic
print(img.shape) #returns a tuple of number of rows,columns,and channels
print(img.size) #returns total number of pixels is accessed
print(img.dtype) #returns image datatype is obtained

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

ball=img[280:340,330:390]     #copy the ball (coordinates of a ball)
img[273:333,100:160]=ball     #paste at this coordinates by assigning


img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

dst=cv2.add(img,img2)     #add images
dst2=cv2.addWeighted(img,.9,img2,.1,0)    #adding using weights
cv2.imshow("add window",dst)
cv2.imshow("add weighted window",dst2)
cv2.imshow('image window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()








""" ROI of image
ROI stands for Region of Interest
 Sometimes we need to work with the certain region of the image.
 ex: work with ball, work with face

 Get coordinates of a particular region to work
"""
