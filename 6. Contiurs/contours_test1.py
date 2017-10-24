import cv2
import numpy as np

# Load video
img = cv2.imread('../img/contour_img.jpg')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow('show', img)
k = cv2.waitKey(5) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
