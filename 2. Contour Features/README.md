#圖形辨識

此筆記藉由圖形辨識這一題目練習API使用。

## Threshold

首先，先將256色影像二值化，設定一個`閥值(thrsdhold)`後將大於它的數設為1反之為0。此函式最簡地的使用方式如下

    ret,thresh = cv2.threshold(img,127,255,0)

這是一個Tuple的資料結構宣告，將圖檔img丟入函示，閥值會存入ret變數，處理後的資料存入thresh變數，更詳細的函示說明與參數運用可參考 <http://monkeycoding.com/?p=593>

-----