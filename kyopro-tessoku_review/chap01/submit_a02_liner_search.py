# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_a
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A02.py

import sys

# 数値の取得
N, X = map(int, input().split())
A = list(map(int, input().split()))

for a in A:
    if a == X:
        print("Yes")
        sys.exit(0)
print("No")
