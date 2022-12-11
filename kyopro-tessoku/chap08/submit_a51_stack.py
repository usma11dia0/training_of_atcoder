# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ay
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A51.py

# 教訓：データ構造とは「データの持ち方・管理法」のこと
#       要素が複数を示す場合は、変数名も複数形にする。
#       dequeにて格納された要素の先頭を取得する際は、[-1]を指定する。

from collections import deque

# 入力データ取得
Q = int(input())
queries = [input().split() for i in range(0, Q)]

S = deque()
for q in queries:
    if q[0] == "1":
        S.append(q[1])
    elif q[0] == "2":
        print(S[-1])
    elif q[0] == "3":
        S.pop()
