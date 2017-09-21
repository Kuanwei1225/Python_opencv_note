# 影像處理

這章節會使用很多影像處理的基本概念與數學公式，雖較少實作但極為重要需一一弄懂。

## 色彩空間

常用的顏色表示的抽象數學式有RGB、CMYK和HSB。RGB表示方式是以`紅色為X座標`、`綠色為Y座標`和`藍色為Z座標`，這樣就得到一個三維的色彩表示式。在前面的例子，創建一個黑畫面為

```
img = np.zeros((512, 300, 3), np.uint8)
```

它為一個512x300x3的三維空間，在此可知其原理。因數字都為0，故為黑畫面；因為256色，所以是uint8。


CMYK為青色(Cyan)、洋紅(Magenta)、黃色(Yellow)和黑色(Black) 組成

最後一種為色相（X軸）、飽和度（Y軸）和明度（Z軸）的HSB表達式，色相就專指何種顏色(黃、藍...)；飽和為色彩純度，高則越純、低則越灰；最後就亮度。

HSB和RGB可互相轉換，可以多找一下轉換公式，這裡不多提

### Practice

在test.py中只留下偏紅的色塊，其餘的遮蔽掉。

## 如何得到HSV數值

我們可以直接利用指令得到BGR轉HSV之數值，若你要得到綠色之HSV值，你可以

```
>>> green = np.uint8([[[0,255,0 ]]])
>>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
>>> print hsv_green
[[[ 60 255 255]]]
```

---

## 旋轉與位移

這章節較多數學公式且較少使用，直接看原文

<http://docs.opencv.org/3.1.0/da/d6e/tutorial_py_geometric_transformations.html>

主要有兩個函式分別為位移`cv2.warpAffine`和旋轉`cv2.warpAffine`，都各需要輸入矩陣，因此建議看原文。

---

## 再論Threshold

二值化可說是影像處理相當重要的環節，在之前的使用上是以固定閥值的方式，但opencv提供另外一種適應性閥值(Adaptive Thresholding)函式`cv2.ADAPTIVE_THRESH_MEAN_C`與 `cv2.ADAPTIVE_THRESH_GAUSSIAN_C `。

```
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                 cv2.THRESH_BINARY,11,2)
```

`cv2.ADAPTIVE_THRESH_MEAN_C`是以鄰近區域的平均值作為閥值；`cv2.ADAPTIVE_THRESH_GAUSSIAN_C `是以鄰近區域權重相加，而權重是以高斯函數運算出來的(詳細還需研究)。

### Return value

在之前threshold的用法中有個ret回傳數，在此簡述一下這是什麼。

```
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
```

通常找閥值都是使用試誤法，但opencv可使用Otsu’s Binarization方法找出合適的閥值。若有使用回傳自動找出的閥值、若無則回傳一開始設定的固定閥值。當處理一張有雜訊之圖片時，先使用濾波器再使用Otsu’s Binarization就會得到較佳的效果。

```
blur = cv2.GaussianBlur(img,(5,5),0)
ret3, th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
```

要了解其原理必須知道許多影像處理重要的概念，如像素直方圖、變異數等。Otsu是以像素直方圖為基準找出閥值，此演算法不僅可用於影像處理，只要在`決定門檻值`的情況都能使用。

詳細的原理可參考與google Otsu

<http://docs.opencv.org/3.1.0/d7/d4d/tutorial_py_thresholding.html>

---

## Filter

在one dimensional 之訊號，有低通與高通濾波器。低通幫助去除雜訊、高通用於強化邊緣。

### 原理與動作

濾波器又稱為遮罩(mask)、kernel，為一個單數矩陣(3x3, 5x5....)。首先將矩陣對應到的像素乘上矩陣相對應的權重後相加，最後除上X後替代中間的值，其中X為矩陣上所有的權重相加。原理簡單，詳情可搜尋網路有很多圖形範例。

矩陣越大，平滑、去雜訊效果越明顯，但也會造成影像越模糊。這裡有個範例，建一5x5的矩陣其數值都為1，將數值相加後為25故最後除25，將此矩陣帶入函式即可完成濾波。

```
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
```

### 影像模糊化(Blur)

為了消除雜訊，有時會利用模糊化的技術。這其實就是一種低通濾波器，簡單分為四種形式

1. Averaging：一般的低通濾波器。
2. Gaussian Blurring：以高斯式代替一般式，其矩陣組成之中心有最大值，依常態分佈向四周下降。
3. Median Blurring：演算法與一般濾波演算不一樣，將kernel覆蓋的圖像的值依順序排列，中位數取代圖像中間的值。
4. Bilateral Filtering：雙邊濾波器，保留邊緣，也就是顏色差異太大就不模糊。

在opencv中使用方法為

```
img = cv2.imread('my_image.jpg')
blur = cv2.blur(img, (5, 5))
blur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
blur = cv2.bilateralFilter(img, 9, 75, 75)
```

GaussianBlur的輸入參數0為`標準差`(分佈的坡度)，輸入0為系統自動；medianBlur的輸入參數5單純指這是5x5的`矩陣`；bilateralFilter第一個參數是`矩陣大小`、第二個為`像素色差標準差`，越大代表考慮更多顏色、最後為`空間標準差`越大表越遠的像素權值會變大，這其實與高斯濾波很像，但在此須考慮顏色與距離兩種標準差，而高斯濾波只考慮距離一種。

---

## 影像形態學(Morphological)

有些時候為了處理邊緣、雜訊與凸顯影像特徵的問題會使用這種方法，分別為

1. 侵蝕(Erosion)：減少原有資料，可用於去除雜訊。其原理為kernel內所有值是1就是1，否則會轉為0。
2. 膨脹(Dilation)：擴張原始資料，邊界效果增強。原理和侵蝕相反。
3. 斷開(Opening)：先侵蝕後膨脹。
4. 閉合(Closing)：先膨脹後侵蝕。
5. 型態梯度(Morphological Gradient)：用於強化邊緣。原理為侵蝕與膨脹之差(different)。
6. Top Hat：多用於被光影所影響的細節。其原理為原圖與膨脹之差。
7. Black Hat：分離比鄰近案的區塊，強化陰影輪廓。做法是取原圖與陰影的差。

在opencv中須先建立一個矩陣(kernel)才能帶入函式使用。首先是侵蝕與膨脹，迭代次數越多效果越明顯。

```
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)
```

之後的一起看，使用相同函式只是第二個輸入參數不同。

```
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# Morphological Gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
```

因kernel大小與形狀會影響輸出效果，opencv提供一些矩陣形狀讓使用者選擇不同效果，要使用必須import Numpy

```
# Rectangular Kernel
>>> cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]], dtype=uint8)
# Elliptical Kernel
>>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [0, 0, 1, 0, 0]], dtype=uint8)
# Cross-shaped Kernel
>>> cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0]], dtype=uint8)
```














