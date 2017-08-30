## 小實驗

一些練習。

## Mouse brush

定義背景函式，在此輸入參數會由系統自動填入，若缺少會不能執行。事件有很多選想可以選。在實作時`EVENT_LBUTTONDBLCLK`做不太出來，因此改為`EVENT_MOUSEMOVE`，之後可以多試試。

```
def draw_circle(event, x, y, flags, param ):
   if event == cv2.EVENT_MOUSEMOVE :
      cv2.circle(img, (x, y), 10, (0, 255, 0), -1)
```

利用函式設定背景執行。

```
cv2.setMouseCallback('image', draw_circle)
```

完整

```
import cv2
import numpy as np

# mouse callback function

def draw_circle(event, x, y, flags, param ):
   if event == cv2.EVENT_MOUSEMOVE :
      cv2.circle(img, (x, y), 10, (0, 255, 0), -1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27: # ESC
        break
cv2.destroyAllWindows()
```

## Trackbar

利用`Trackbar`做出改變顏色的效果。第一個參數為trackbar的名子；第二個為出現視窗的名子；第三與第四個參數為數字範圍；第五個為背景執行程式，在這裡沒有用所以填入空函式。

```
cv2.createTrackbar('R', 'image', 0, 255, nothing)
```

利用`cv2.getTrackbarPos('R','image')'來獲得指定TrackBar的參數。

全部：

```
import cv2
import numpy as np

def nothing(x):
    pass
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')
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
    # change color
    img[:] = [b, g, r]
cv2.destroyAllWindows()
```

## 練習

試著將兩個練習合起來。






