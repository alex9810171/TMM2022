# NTU EduTch Teaching Methods and Materials - 2022
## Author information
- Alex Hsu
- Email: alex9810171@gmail.com

## Lecture Note
- story telling for one topic.
- 事先準備好，除非有一些是臨場demo的效果更好
### 2023.05.11 RSA Demo
- 定義放在黑板左側
- 把example放在黑板右側
    > 定義 ... Pf ... Example
    >
    > 定理 ... 定理2
    > 
    > 定義
- 先講簡單的例子，再推導到困難的部分
    > 定義 -> 例子 -> 定理 -> 例子 -> 證明 -> 例子
- 需要停頓讓學生思考
- 注意力只能撐40分鐘，後面就會變成在抄筆記
- 要不要留一些資訊，還是擦掉？
- 估算黑板長度，有些可以寫3段，有些可以寫更多or少



## Note
1. 20230323_insertion_sort_exercise
- Goal: Sort student from 1 2 3 4 5 to 1 5 2 4 3
- test type: random*2, order*2, reverse*2, almost-order*2, almost-reverse*2
2. 20230411_mosaic_exercise
- Goal: bin several pixels into one pixel
- test type:
```
6 4
34 154 213 36 197 118
234 184 167 38 223 134
173 82 31 152 149 253
161 40 27 235 127 158
```
3. 20230422_bucket_problem
4. 20230426_nonogram
```
python3 main.py -m 1 < stage_3_in/00.in > stage_3_out/00.out
python3 main.py -m 2 -i test/06_b.png -t 15 -s stage_1_ans/06.png
```
5. 20230426_histogram
```
python3 main.py -m 1 -s stage_3_out/hist_00.png < stage_3_in/00.in > stage_3_out/00.out
```