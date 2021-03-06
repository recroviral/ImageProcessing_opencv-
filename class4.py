import numpy as np
import cv2

img = cv2.imread("2.jpeg",1)

#scale
img_half = cv2.resize(img,(0,0), fx=0.5, fy=0.5)
img_stretch =cv2.resize(img, (600,600))
img_stretch_near = cv2.resize(img, (600,600), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Half",img_half)
cv2.imshow("Stretch",img_stretch)
cv2.imshow("Stretch_Near",img_stretch_near)

#Rotation
M = cv2.getRotationMatrix2D((0,0), -90, 1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow("Rotated",rotated)

cv2.waitKey(0)
cv2.destroyAllWindows
