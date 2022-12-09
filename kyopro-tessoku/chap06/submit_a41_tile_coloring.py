# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ao
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap06/answer_A41.py

# 教訓：最後から考える。最終的に、連続する3つのタイルが同じ色となる箇所があるかどうかを判定する問題へ帰着させる。

import sys

# 入力データ取得
N = int(input())
S = str(input())
S_list = []
for s in S:
    S_list.append(s)

# 連続する3つのタイルが同じ色となる箇所があるかどうかを判定
for i in range(0, N - 2):
    if S_list[i] == S_list[i + 1] == S_list[i + 2]:
        print("Yes")
        sys.exit(0)
print("No")
