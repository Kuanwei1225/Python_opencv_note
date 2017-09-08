# Core operation

在此介紹一些opencv的核心運算。

### 存取特定像素

得到RGB值

```
pix = img[100, 100]
print(pix)
```

得到藍色值

(100, 100)為象素

```
blue = img[100, 100, 0]
print(blue)
```

直接存取

```
img[100, 100] = [255, 255, 255]
```

## 複製其中一塊並貼上

```
block = img[100:150, 200:250] # copy
img[300:350, 450:500] = block # paste
```

### 分離與融合出BGR

```
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
```

or

```
b = img[:, :, 0]
```

---

## 圖片相加

2張圖片要相加必須相同大小和型別(在此都為256色)。

```
>>> x = np.uint8([250])
>>> y = np.uint8([10])
>>> print cv2.add(x,y) # 250+10 = 260 => 255
[[255]]
>>> print x+y          # 250+10 = 260 % 256 = 4
[4]
```

## 圖片混和(Blending)

將不同權重圖片混和，其概念如下式所示，α介於0~1之間。

g(x)=(1−α)f0(x)+αf1(x)

接著介紹`addWeighted()`，其概念公式如下

dst=α⋅img1+β⋅img2+γ

在此設定，α = 0.7，β = 0.3

```
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
```
## Threshold

將256色影像二值化，設定一個`閥值(thrsdhold)`後將大於它的數設為1反之為0。此函式最簡地的使用方式如下。閥值設為127，小於127設為0，大於則設為255。

    ret,thresh = cv2.threshold(img,127,255,0)

這是一個Tuple的資料結構宣告，將圖檔img丟入函示，閥值會存入ret變數，處理後的資料存入thresh變數，更詳細的函示說明與參數運用可參考 <http://monkeycoding.com/?p=593>

-----

## 位元運算

這裡以一個小實作來說明位元運算。我要用一張小圖片logo印在背景的左上角。

首先先切下和logo等大的圖片。

```
rows, cols, channels = imgLogo.shape
logo = img1[0:rows, 0:cols]
```

接著將影像灰階處理，在二值化後得到遮罩mask，在此須調整閥值，必須只留下中間的logo。

```
imgGray = cv2.cvtColor(imgLogo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(imgGray, 150, 255, cv2.THRESH_BINARY)```
```

介紹一下位元運算函示

@ param src1, src2：兩個要進行位元運算的來源圖
@ param dst：output
@ param mask：輸入遮罩，若無，則不用此參數，若有則以`mask = myMask`的形式輸入。

```
bitwise_and(src1, src2, dst=None, mask=None)
```

用以下手法去背，要注意遮照順序。

```
mask_inver = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(logo, logo, mask = mask)
imgLogo_fg = cv2.bitwise_and(imgLogo, imgLogo, mask = mask_inver)

dst = cv2.add(img1_bg, imgLogo_fg)
```

最後重新寫回左上角。

```
img1[0:rows, 0:cols] = dst
```

---

## 計算程式效率

在此介紹一些計算程式執行時間APIs語最佳化之方法。

計算經過多少tick後除時脈就可以得到執行時間。

```
e1 = cv2.getTickCount()
# your code execution
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
```

## 增加程式效率的小技巧

1. 在Python中減少使用迴圈，特別是double/triple之型別。

2. 使用向量時盡量使用numpy與opencv之API，因為有最佳化過。

3. 注意快取。

4. 最好不要複製陣列，他是一個消耗很高的指令。














