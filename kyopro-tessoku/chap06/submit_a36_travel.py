# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_aj
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap06/answer_A36.py

# 教訓：

import sys

# 入力データ取得
N, K = map(int, input().split())

# Kの手数が足りないか確認
if K >= 2 * N - 2:  # "-2"はスタートのマスとゴールのマスを差し引いている。
    if K % 2 == 0:  # 偶数であればスタートと同じ色のマスへ到着できる。
        print("Yes")
        sys.exit(0)

print("No")
