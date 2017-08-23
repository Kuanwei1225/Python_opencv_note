# 第一支opencv程式
讀取圖片並顯示

1.讀取圖片，路徑最好用相對路徑

```
img = cv2.imread('../XXX/MyImg.jpg')
```

2.建立顯示視窗

```
cv2.namedWindow("Display image", cv2.WINDOW_AUTOSIZE)
```

3.顯示圖片

```
cv2.imshow('Display image', img)
```

3.等待鍵盤輸入，若沒這指令會瞬間顯示後關掉，而不會卡住

```
cv2.waitKey(0)
```

4.複製圖片

```
myImg = img.copy()
```

5.存檔

```
cv2.imwrite('../testSave.jpg', myImg)
```

----
## 一些小應用

打開一張圖片，如果按ESC就離開；按`s`就存檔。

```
import cv2
import numpy as np

# read the image file
img = cv2.imread('../img/TestImg.jpg')
cv2.imshow('Show Image', img)
k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('../copyimg.png', img)
    cv2.destroyAllWindows()
```

---

## 使用matplotlib

opencv使用BGR顯示，但matplotlib是使用RGB顯示，因此顏色會些許不同。

```
plt.imshow(img)
# hide tick values
plt.xticks([])
plt.yticks([])
plt.show()
```

----
## 讀取影片

使用`VideoCapture`物件來抓取影片，指定影片則輸入路徑若無則輸入`0`，輸入`0`時代表影片來源為攝影機。

```
cap = cv2.VideoCapture('./MyVideo')
```

再撥出之前可確認初始化是否完成，使用`cap.isOpened()`。

可使用`cap.get(3)`與`cap.get(4)`獲得長寬比，使用攝影機時可利用` ret = cap.set(3, 320)`與` ret = cap.set(4, 620)`設定畫質。

```
import cv2
import numpy as np

cap = cv2.VideoCapture('test.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
```

使用迴圈包住，如此可撥出影片。值得注意的是`cv2.COLOR_BGR2GRAY`可更改，但有時影片不支援或不明原因有些模式會無法使用。

----
## 影片存檔










