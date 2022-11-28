# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_z
# answer

# 教訓：

import sys

# 入力データの取得
Q = int(input())
X = [int(input()) for _ in range(0, Q)]

for x in X:
    flag = False
    for i in range(2, x):
        if (x % i) == 0:
            flag = True
            break
    if flag == False:
        print("Yes")
    else:
        print("No")
