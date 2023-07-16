## 1. VS Code Environment: Utilities for Development
- First, we can talk about programming for newers.
### (1) GitHub 教學
- Create git and GitHub. 
    
    (You can sign up github education so that you will have private respon privacy.)
- Install Github desktop
- Try to create and push repo.
    ```markdown
    # Git note
    ## Initial setting
    git init (by VS Code)
    git remote add origin "your url"
    git add .
    git commit -m "first commit"
    git branch -M main

    ## Download
    git pull origin main

    ## Upload
    git add .
    git commit -m "first commit" / git commit -m "update"
    git push -u origin main
    ```
- 先開準備放程式的資料夾 （記得資料夾用英文檔名）
- 然後去GitHub開一個同名稱的repo
- 供參考：<https://ithelp.ithome.com.tw/articles/10280309>
- 檔案的命名不要用中文or空格，會在Linux系統上出事
- 講解正確的repo命名方式
    - 資料夾名稱請用大寫開頭
    - 裡面的檔案才用小寫
    - 中間用"-"隔開
- git指令講解
    ```markdown
    # git init
    - 我們為了要建立一個檔案變更的紀錄檔，所以要在資料夾底下開一個git資料夾來記錄，也就是建立.git資料夾
    # git add
    - 他是要把你的檔案變更紀錄更新到.git資料夾內
    - 如果是git add .  則是把資料夾底下所有的更新紀錄都放到.git資料夾
    - 如果只有git add "檔案名稱"  則只有更新指定的檔案
    # git commit
    - 針對你的這次更新紀錄，建立一個備註
    - 所以有些人會利用這個備註，來知道每一次更新在幹嘛
    - but，因為寫這個東西不夠詳細or清楚，所以才有CHANGLOG的誕生
    <https://keepachangelog.com/zh-TW/0.3.0/>
    # git branch
    - 就是一個repo可以建立好幾種不同版本的程式分支，而我們目前只會用到主分支，也就是main
    - 所以只要在第一次建立repo的時候設定git branch -M main就可以了
    # git remote
    - 就是連結你的本地git資料夾到網路上的github
    - 所以也是第一次的時候設定，git remote add origin "your url"即可
    # git push -u origin main
    - 把你的git更新資料以及檔案上傳到main分支上面
    - GitHub 限制單一檔案 100 MB 的限制
    - 所以這時候就需要交由 LFS 這個功能來上傳到github上面
    - 詳情可參考 <https://ithelp.ithome.com.tw/articles/10229654>
    # 如何把github上面的repo下載到本地端
    - 可能之前有試過直接用zip下載
    - 但後面會有一個問題就是沒有git init
    - 所以我們一般會建議，先開一個相同名稱的資料夾，然後：
        - git init
        - git remote
        - 最後使用git pull origin main來把main分支的檔案下載下來
    ```
- QA Time:
    - Q1: 那之後更新還要再add origin "your url"嗎?
    - A1: 不用，因為你已經把你的本地端git資料夾連結到github上面了，他會記錄在.git資料夾裡面的config檔案裡面
    
### (2) .gitignore 教學
- 我們在前面不是有提到"GitHub 限制單一檔案 100 MB"，那如果我的資料夾底下有大於100MB的檔案不想上傳怎麼辦？
- 這個時候就要用.gitignore的檔案來把指定的檔案忽略不要上傳
    ```markdown
    - 如果我要省略一個檔案的話就直接用test.py
    - 省略一類檔案就用*pt
    - 省略資料夾底下的檔案就可以用 folder/
    ```
- README.md跟.gitignore是構成一個repo的重要檔案
- 個別的資料夾底下也有我不想要的特定檔案就再開一個專用的.gitignore檔案
- QA Time:
    - Q1: 突然想到 git add.是要接資料夾名稱嗎?
    - A1: 不用
    - Q2: git pull origin main 是下載在main分支上的同名檔案?
    - A2: 對的
    - Q3: 就是分不同類型的檔案，或是單一個檔案忽略對吧
    - A3: 對，也可以忽略特定資料夾底下的所有檔案，畢竟人家叫做git ignore，ignore = 忽略
### (3) README.md 教學
- readme就是類似記事本的概念，他可以當你自己的筆記，也可以給別人看你的這個repo在做什麼（github有時候會被叫做筆記本存放區）
```markdown
#是第一層標題
##第二層
###第三層
最多可以6個#
* 文字 （*後面接一個空格）
```
- Markdown語法說明: 
    - <https://markdown.tw/>
    - <https://hackmd.io/@eMP9zQQ0Qt6I8Uqp2Vqy6w/SyiOheL5N/%2FBVqowKshRH246Q7UDyodFA?type=book>
- README.md用的是"m"ark"d"own格式，就是高級版的txt
- 如何預覽readme的教學