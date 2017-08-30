import cv2
import numpy as np

r, g, b = 0, 0, 0

def nothing(x):
    pass

def draw_circle(event, x, y, flag, param):
    global r, g, b
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (b, g, r), -1)

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
# create trackbars 
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

while(True):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27: # ESC
        break
    # get current positions
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
cv2.destroyAllWindows()