## 2. Stucture Project Hierarchy and Naming Conventions
### (1) Project的經典格式
- 首先要講解檔案的命名方式 and 一個project的經典格式（舉例說明）
    ```
    doc/
    src/
    test/
    README.md
    .gitignore
    ```
- doc是拿來存放一些說明這個project的文件用的
- src是存放程式碼
- test是存放測資或者是讓使用這個project的人測試project的功能用的
- 其他的一定會有gitignore, README跟LICENSE
    - LICENSE則是其他人使用這個程式碼要注意的規範，例如不得商用之類的
### (2) 變數的命名規則
- 變數的命名規則，可參考 <https://medium.com/%E7%A8%8B%E5%BC%8F%E6%84%9B%E5%A5%BD%E8%80%85/%E8%AE%8A%E6%95%B8%E5%91%BD%E5%90%8D-f53cd1115076>
    ```markdown
    截取重要的部分來講
    - 命名習慣的好壞可由以下2點判斷:
    1. 可讀性
    2. 一致性
    - 可讀性就是不要abcdefg，或者是a1 a2 a3 a4 a5
    - 正常的命名應該要是
        int length = 10;
        bool isEmpty = true;
        或者也可以is_empty
        function的部分用小寫開頭
        class用大寫開頭
        Const有些會用全大寫，const char NAME = "a"
    ```
- 這部分會幫助你之後在寫比較長的程式時，盡量的避免變數混淆的問題
- 此外，VS Code也有重新命名符號的功能，可以讓你一次改同一個變數的所有名稱
### Terminal的基本指令
- 這部分比較偏記憶，只要記得常用的指令就行了
    ```markdown
    ls 列出資料夾下的所有檔案
    rm file 移除指定檔案
    rm -rf folder 移除資料夾下的所有檔案
    top 叫出linux的工作管理員
    ./a.exe 執行檔案
    ./a.exe < 1.in > 1.out 把1.in的檔案作為a.exe的輸入，然後輸出到1.out上面（解題的時候常用）
    gcc test.c compile test.c變成可執行的檔案
    python的話則是直接python test.py就可以執行
    ```
- 所以你會發現我們可以利用一些指令去做圖形化介面沒有給的功能
- 此外也可以給一些參數
    ```markdown
    python3 tools/train.py \
    -f exps/yolov/yoloxs_vid.py \
    -c ../../models/YOLOX/yolox_s.pth \
    -b 16 --fp16
    ```
    - 執行tools資料夾下train.py的檔案
    - 然後-f -c -b -fp16都是給train.py的參數
- QA Time:
    - Q1: 這個 1.in 跟 1.out是甚麼意思，資料夾名稱嗎?
    - A1: 例如zerojudge，上傳程式的時後他會檢查你的程式對不對，用到的就是1.in，裡面有測資，然後比對輸出正不正確，比對的方式就是他有一個標準解答1.out，然後看你的答案有沒有跟1.out吻合
        - 例如，比對你的程式輸入00.in之後的輸出有沒有跟00.out一致，如果有才會AC
    - Q2: 參數是甚麼
    - A2: ```int a = 100```，我們可以在執行程式前給a=100這個值，或者```int a```，然後執行時才給a=100
    - Q3: rm -rf是資料留著但裡面檔案消失?
    - A3: 連同資料夾一起砍掉，rm file則是砍檔案，如果拿來砍資料夾會報錯

- Homework 0