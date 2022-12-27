# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_c
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A02.py

import sys

# 入力データの取得
N, K = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# 合計値の初期化
total = 0

for p in P:
    total = p
    for q in Q:
        total += q
        if total == K:
            print("Yes")
            sys.exit(0)
        # totalの値をpに戻す
        total = p
print("No")
