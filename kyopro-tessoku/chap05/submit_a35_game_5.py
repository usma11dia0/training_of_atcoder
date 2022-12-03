# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ai
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap05/answer_A35.py

# 教訓：逆から考える事も有効
#       配列のインデックスを扱う際は要素0の扱いに細心の注意を払う。

import sys

# 入力データの取得
N = int(input())
A = list(map(int, input().split()))

# dp[i][j] : 両プレイヤーが最善の手を尽くした場合の得点
# i:ピラミッドの段数
# j:左から数えた番号

# dpの初期化 indexに注意 [0] = 1
dp = [[0] * (N + 1) for i in range(0, N + 1)]

# DP(N段目)
for j in range(1, N + 1):
    dp[N][j] = A[j - 1]


# 貰うDPを定義する ※最下段から上段へ移る点に注意
for i in range(N - 1, -1, -1):
    for j in range(1, i + 1):
        if i % 2 != 0:  # iが奇数だった場合は太郎君の番(最大化)
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])
        else:  # iが偶数だった場合は次郎君の番(最小化)
            dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1])

print(dp[1][1])
