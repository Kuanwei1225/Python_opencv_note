import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (10, 0), (511, 511), (255, 0, 0), 5)

cv2.rectangle(img, (450, 0), (510, 128), (0, 255, 0), 3)
cv2.circle(img,(400,63), 63, (0,0,255), -1)
cv2.ellipse(img, (256, 256) , (150, 100), 0, 0, 180, 255, -1)

pts = np.array([[10,10], [20,30], [150,20], [50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

txt = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Test', (10, 500), txt, 8,(255,255,255), 2, cv2.LINE_AA)

cv2.imshow('show', img)
cv2.waitKey()
cv2.destroyAllWindows()