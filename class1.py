import numpy as np
import cv2

color = cv2.imread("2.jpeg",1)
cv2.imshow("Image",color)
cv2.moveWindow("Image",0,0) # window will open in top left hand corner
print(color.shape)
height,width,channels = color.shape

b,g,r = cv2.split(color)


rbg_split = np.empty([height,width*3,3],'uint8') #uninitialized array matrix

rbg_split[:, 0:width] = cv2.merge([b,b,b])
rbg_split[:, width:width*2] = cv2.merge([g,g,g])
rbg_split[:, width*2:width*3] = cv2.merge([r,r,r])

cv2.imshow("channels",rbg_split)
cv2.moveWindow("channels",0,height) #move window

hsv =cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v =cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)
cv2.imshow("Split HSV",hsv_split)
 

cv2.waitKey(0)
cv2.destroyAllWindows()
