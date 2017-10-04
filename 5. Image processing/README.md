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

二值化可說是影像處理相當重要的環節，在之前的使用上是以固定閥值的方式，但opencv提供另外一種適應性閥值(Adaptive Thresholding)函式`cv2.ADAPTIVE_THRESH_MEAN_C`與 `cv2.ADAPTIVE_THRESH_GAUSSIAN_C `。在陰影處理上，若是固定閥值會誤判陰影部分，用此方法會較容易去除此影響。

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

---

## 梯度

取得邊緣一直是重要課題，當灰階值有劇烈變化時就會認為他為邊緣。常用的方法為取梯度，計算方法為kernel對應到的格子內數值相減，若超過閥值便判斷為邊緣。常用的1st 微分為Sobel operator，可藉由不同的kernel 排列來找出垂直或水平的邊緣，kernel與影像作旋積後可得到X軸的梯度與Y軸的梯度將兩者用歐式距離相加即可得到邊緣，算出來的結果可能為負。第二個參數維影像深度、第三第四分別為對x軸偏微分與對y軸之偏微分。只對一軸偏微分表只取橫向(或縱向)之邊緣。

```
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
```

###  Laplacian Derivatives

使用Laplace運算子來搜尋邊界，若沿著x軸的一次微分可寫成

```
df = f(x+1, y) - f(x, y)
```

再一次微分，也就是兩次可寫成

```
d2fx = [ f(x+2, y) - f(x+1, y) ] - [f(x+1, y) - f(x, y)]
    = f(x+2, y) - 2f(x+1, y) + f(x, y)
while x = x + 1 change the equation
    =f(x+1, y) - 2f(x, y) + f(x-1, y)
```

得到兩次偏微分，同理可求對y軸偏微分。最後帶入拉普拉斯運算式即可。將其向x、y軸展開，可以近似於<http://docs.opencv.org/3.3.0/d5/d0f/tutorial_py_gradients.html>的kernel形式，最後將kernel與影像旋積(convelution)。

```
laplacian = cv2.Laplacian(img,cv2.CV_64F)
```

在此有一點須注意，當你輸出圖像深度為CV_8F，也就是uint8時。因為在判斷邊緣時使用梯度(斜率)，其值有可能為負(白-黑)，此時負值會變為0在圖面上無法顯示，因此會偵測不到。

---

## Canny Edge Detection 

找邊緣常與雜訊作取捨，此種方法先使用高斯平滑去除雜訊後再找邊緣，有較佳的效果，其步驟為(自我了解，這東西非常複雜)

1. 使用高斯平滑去除雜訊
2. 使用一階梯度找邊緣(Sobel, Roberts)找出強度與方向。
3. 非最大值抑制，也就是說若該點為區域最大值那他很有可能就是邊緣，此時留下最大值數據，其餘歸零。
4. 跟蹤邊緣，假設由上步驟算出來的值位於大於max threshold，那可稱之為邊緣；若在max threshold與min threshold之間，而前後為邊緣，那他也是邊緣；雖然他在max threshold與min threshold之間但前後不為邊緣，那他不是邊緣。

在opencv可使用`cv2.Canny`達成。第一個參數為`原始圖片`、2跟3為`閥值的上下限`。

```
img = cv2.imread('picture.jpg',0)
edges = cv2.Canny(img, 100, 200)
```

---

## 影像金字塔(Image Pyramids)

有時候需要影像的不同解析度，比如說要搜尋某些圖片時，因為不知道原始圖片的大小，藉由比較多維圖片防止內容與圖片上大小不同，所以會使用這種同圖片不同解析度的方式稱為影像金字塔(Image Pyramids)。影像金字塔有兩種形式

1. Gaussian Pyramid：使用高斯模糊後將影像長與寬縮小(或放大)2倍(二分之一取樣)。但還是表示同樣範圍。
2. Laplacian Pyramids：先用得到高斯金字塔後比較這層與上一層，得到高頻數據(多是邊緣)，而其餘資料都為0，多用於影像壓縮。

opencv之用法，參數就是要建成金字塔之圖片，值得注意的是取樣會失去部分資訊，因此再放大也不會得到原始圖片。

```
img = cv2.imread('img.jpg')
lower_reso = cv2.pyrDown(higher_reso)
higher_reso2 = cv2.pyrUp(lower_reso)
```

laplacian金字塔並沒有相對應的函式，所以可以這麼做

```
img = cv2.imread('picture.jpg')
# create a guass pyramids
cc = img.copy()
arr = [cc]
for i in range(6):
    cc = cv2.pyrDown(cc)
    arr.append(cc)
## create laplacian pyramids
lp = [arr[5]]
for i in range(5, 0, -1):
    gg = cv2.pyrUp(arr[i])  # get upper level
    L = cv2.subtract(arr[i-1], gg) # calculate laplacian
    lp.append(L)
```

要注意的是，因up level是計算出來的，有時候會因解析度不相符而無法相減。

ps. 延伸：影像融合<http://docs.opencv.org/3.3.0/dc/dff/tutorial_py_pyramids.html>

---

















