# BeatingClock 打人鬧鐘

## 題目發想起源
  　冬天到了，要從暖暖的床舖裡起床總是一件折磨人的事，想要解決室友賴床毛病的我們，決定要做一個既可以無限甩巴掌，也可以播振奮人心音樂的鬧鐘。

## 所需材料
 材料名稱 | 數量 | 單價 | 總價 | 來源
------------ | ------------- | -------------| -------------| -------------:|
杜邦線（公母）|			30條（3片）|			$11|			$33|			露天網購|
杜邦線（公公）|			ｎ條|			-|			-|			MOLI提供|
伺服馬達（MG995）|			1個|			$200|			$200|			露天網購|
顯示器（QC1602A）|			1個|			-|			-|			小鮮肉學長熱情提供|
麵包版|			1片|			-|			-|			MOLI熱情贊助|
小麵包版|			1片|			$19|			$19|			露天網購|
白手套|			1雙|			$25|			$25|		  圖文部|
棉花|			1包|			$35|			$35|			墊腳石|
電阻|			3個|			-|			-|			MOLI熱情贊助|
按鈕|			3個|			$4|			$12|			露天網購|
蒼蠅拍|			1隻|			$15|			$15|			圖文部|
可變電阻|			1個|			-|			-|			小鮮肉學長熱情提供|
音響|			1個|			-|			-|			茂林TA熱情提供|
螺絲墊片|			2片|			-|			-|			保保學長熱情提供|
螺帽|			2個|			-|			-|			保保學長熱情提供|
Raspberry pi|			1個|			-|			-|			課程提供|

## 運用與課程內容中相關的技巧
 1. Raspberry pi 相關操作
 2. 使用mail自動寄IP
 3. Github 操作
 4. ssh

## 使用的現有軟體與來源
 - Python
 - RPI.GPIO 函式庫
 - pygame 函式庫



## 實作過程
### 計畫
 1. 需要打人：棉花手掌、馬達
 2. 需要顯示器：顯示倒數時間
 3. 需要按鈕：（1）確認鈕 （2）時間向上調按鈕 （3）時間向下調按鈕
 4. 需要鈴聲：音響

### GPIO設置

 - GPIO參考圖

 ![GPIO](https://github.com/NCNU-OpenSource/BeatingClock/raw/master/image/GPIO參考.png)

　　因為使用Python撰寫程式，引入RPI.GPIO函式庫。參考此圖，以連結我們所需的GPIO。
 - 顯示器接法

 ![顯示器](https://github.com/NCNU-OpenSource/BeatingClock/raw/master/image/顯示器連結.png)

 顯示器接法參考[此連結](http://raspberrypi.powersbrewery.com/project-10-16x2-lcd-alarm-clock-with-buzzer)，並依照我們的需求做調整。
 - 按鈕接法

 ![按鈕](https://github.com/NCNU-OpenSource/BeatingClock/raw/master/image/按鈕連結.jpg)

 按鈕接法參考[此連結](https://sites.google.com/site/raspberrypidiy/basic/gpioinput)。我們需要三顆按鈕，使用了pin#8、pin#11、pin#13。
 - 馬達接法

  ![馬達](https://github.com/NCNU-OpenSource/BeatingClock/raw/master/image/馬達連結.png)

### 過程
 1. 設定GPIO
 2. 接上設備
 3. 音樂播放器的code
 4. 實作馬達code
 5. 馬達配合按鈕code
 6. 顯示器倒數時間的code
 7. 開機自動執行設定
 8. 手的製作
 9. 手與馬達的接合調整
 10. 外部包裝製作
   ![組裝](https://github.com/NCNU-OpenSource/BeatingClock/raw/master/image/組裝.jpg)

# 手把手教學

## 直接使用

### 把檔案download下來
```
git clone https://github.com/NCNU-OpenSource/BeatingClock.git
```
### 接好相關設備
 - 馬達
 - 音響
 - 顯示器
 - 按鈕

### 執行
```
sudo python Test.py
```

## 更改設定

### 更改顯示器所使用的PIN腳
```
vim Adafruit_CharLCD.py
```
 - 更改56行，調整顯示器所需的pin腳

### 新增音樂隨機播放
```
vim Test.py
```
 - 將音樂丟進music資料夾，且更改第8行，將音樂檔的路徑放入，即可隨機播放

### 更改其餘設定（馬達、按鈕所需PIN腳）
```
vim Test.py
```
 - 13行 更改確認鈕的pin腳
 - 14行 更改上調時間鈕的pin腳
 - 15行 更改下調時間鈕的pin腳
 - 16行 更改馬達訊號傳輸pin腳  

# 成品
   ![成品圖](https://github.com/NCNU-OpenSource/BeatingClock/raw/master/image/成品圖.jpg)
