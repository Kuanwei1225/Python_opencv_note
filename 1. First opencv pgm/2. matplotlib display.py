# tThe first opencv project using python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image file
img = cv2.imread('../img/TestImg.jpg')
plt.imshow(img)
# hide tick values
plt.xticks([])
plt.yticks([])
plt.show()



