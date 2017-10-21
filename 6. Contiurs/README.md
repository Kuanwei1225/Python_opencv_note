# Contours 

在opencv中要找出輪廓是使用黑白，要找的`物件須用白色`而`背景要為黑色`。要找出contours使用方法如下，第一個參數為原始圖案；第二個為contour retrieval mode；第三為contour approximation method。

```
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```

接著將它畫出來，第一個為原始圖案，他會直接將輪廓印在上面；第二個為剛剛找到輪廓，可能會有好幾個，可以用debug介面看；第三個為要印出第幾個輪廓，-1為印出全部；接著就是輪廓的顏色。程式可看test1。

```
cv2.drawContours(img, contours, -1, (0,255,0), 3)
```

有時圖形較簡單，並不需要將全部的點都找出只需列出關鍵的即可，這樣也可以節省記憶體，這也是`cv2.CHAIN_APPROX_SIMPLE`做的，若圖形複雜可使用`cv2.CHAIN_APPROX_NONE`。