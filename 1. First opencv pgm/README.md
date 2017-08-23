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













