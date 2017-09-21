import cv2
import numpy as np

# Load video
img1 = cv2.imread('../img/testImg.jpg')
# define range of blue color in HSV
lower_red = np.array([0, 70, 50])
upper_red = np.array([170, 255, 255])

hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_red, upper_red)
mask = cv2.bitwise_not(mask)
# Bitwise-AND mask and original image
res = cv2.bitwise_and(img1, img1, mask = mask)
   
cv2.imshow('frame' ,img1)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
k = cv2.waitKey(5) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
