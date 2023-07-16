## 5. Array
- 1D array
    - Try to initial 1D array with student score:
        ```cpp
        int a[10] = [90, 95, 91, 98, 60,
                    71, 91, 31, 80, 85];
        ```
    - Try to sort above scores from large to small:
        ```cpp
            // TO_DO
        ```
- 2D array
    - Intitial 2D array:
        ```cpp
        int a[6][8];
        ```
        - Q1: 請問直排有幾欄？橫排有幾列？
            8欄 and 6列
        - Q2: 請問要怎麼用2維陣列儲存下列的資料呢？
            ```
            1 2 3 4
            2 5 6 8
            3 4 2 1
            ```
            ```cpp
            int a[3][4];
            ```
        - 因為實際上2維陣列是由多個一維陣列所組成
            ```
            [3] -> 一維陣列數量
            [4] -> 一維陣列
            ```
    - 有了基本的概念之後我們來講讀入跟輸出
        - 讀取
            ```cpp
            int a[3][4];
            for(int i=0; i< 3; i++){
                for(int j = 0; j < 4; j++){
                    // scanf("%d", &a[i][j]);
                    cin >> a[i][j];
                }
            }
            ```
        - 輸出
            ```cpp
            for(int i=0; i< 3; i++){
                for(int j = 0; j < 4; j++){
                    // printf("%d", a[i][j]);
                    cout << a[i][j] << " ";
                }
                // printf("\n");
                cout << "\n";
            }
            ```
    - 練習題講解：
        https://jmj.cmgsh.tp.edu.tw/ShowProblem?problemid=a236
    - HW1講解投影片：
        https://docs.google.com/presentation/d/1ji7-HFEu3OM4QD76qtaJScF9Bmq-lGHJ8j3VkqV4Rss/edit?usp=sharing
