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

要了解其原理必須知道許多影像處理重要的概念，如像素直方圖、變異數等。Otsu是以像素直方圖為基準找出閥值，此演算法不僅可用於影像處理，只要在`決定門檻直`的情況都能使用。

詳細的原理可參考與google Otsu

<http://docs.opencv.org/3.1.0/d7/d4d/tutorial_py_thresholding.html>

---

## Filter

在one dimensional 之訊號，有低通與高通濾波器。低通幫助去除雜訊、高通用於尋找邊緣。





