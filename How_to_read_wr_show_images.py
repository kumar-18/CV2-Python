import cv2

img=cv2.imread('images/lena.jpg',0)   #Reads an image
print(img)    #Prints Pixels of image img

cv2.imshow("Name of Window",img)    #Display image
k=cv2.waitKey(5000)         #Time to display image window(milliseconds)

if k==27:
    cv2.destroyAllWindows()    #CLick ESC  to Destroy all windows
elif k==ord('s'):            #Click S to Save
    cv2.imwrite("lena_1.jpg",img)            #Writes an image in file location
    cv2.destroyAllWindows()    #Destroy all windows
