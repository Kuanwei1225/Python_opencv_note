import cv2
import numpy as np

# Load image
img1 = cv2.imread('../img/testImg.jpg')
imgLogo = cv2.imread('../img/logo.jpg')

# get my logo
rows, cols, channels = imgLogo.shape
logo = img1[0:rows, 0:cols]

# create different color logo
imgGray = cv2.cvtColor(imgLogo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(imgGray, 150, 255, cv2.THRESH_BINARY)
mask_inver = cv2.bitwise_not(mask)
 
img1_bg = cv2.bitwise_and(logo, logo, mask = mask)
imgLogo_fg = cv2.bitwise_and(imgLogo, imgLogo, mask = mask_inver)

dst = cv2.add(img1_bg, imgLogo_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()