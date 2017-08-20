# tThe first opencv project using python
import cv2

# read the image file
img = cv2.imread('../img/TestImg.jpg')

# create a window
cv2.namedWindow("Display image", cv2.WINDOW_AUTOSIZE)

# show the image
cv2.imshow('Display image', img)

# show the image until any keybroad input
cv2.waitKey(0)
