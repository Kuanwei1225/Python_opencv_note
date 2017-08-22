# 第一支opencv程式
讀取圖片並顯示</br>

1.讀取圖片，路徑最好用相對路徑</br>
<pre><code>img = cv2.imread('../XXX/MyImg.jpg')
</pre></code></br>

2.建立顯示視窗</br>
<pre><code>cv2.namedWindow("Display image", cv2.WINDOW_AUTOSIZE)
</pre></code></br>

3.顯示圖片</br>
<pre><code>cv2.imshow('Display image', img)
</pre></code></br>

3.等待鍵盤輸入，若沒這指令會瞬間顯示後關掉，而不會卡住</br>
<pre><code>cv2.waitKey(0)
</pre></code></br>

4.複製圖片
<pre><code>myImg = img.copy()
</pre></code></br>

5.存檔
<pre><code>cv2.imwrite('../testSave.jpg', myImg)
</pre></code></br>
