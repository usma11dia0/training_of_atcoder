# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_o
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap03/answer_A15.py

import bisect

# 入力データ取得
n = int(input())
a = list(map(int, input().split()))

# 配列xの作成 (aにて重複削除 & 並び替え)
x = list(set(a))
x.sort()

# aの各要素が配列xの何番目にあるかを二分探索で導出
for i in range(0, n):
    index = bisect.bisect_left(x, a[i])
    print(index + 1, end=" ")
