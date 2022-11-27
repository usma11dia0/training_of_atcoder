# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_y
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A25.py

# 教訓：

# 入力データの取得
H, W = map(int, input().split())
c = [None] * H
for i in range(H):
    c[i] = input()

# dp[i][j]: マス(1,1)からマス(i,j)まで移動する方法の数
dp = [[0] * (W) for _ in range(0, H)]

dp[0][0] = 1
for i in range(0, H):
    for j in range(0, W):
        # マス(i-1,j) → マス(i,j)に直接移動
        if i > 0 and c[i - 1][j] == ".":
            dp[i][j] += dp[i - 1][j]
        # マス(i,j-1) → マス(i,j)に直接移動
        if j > 0 and c[i][j - 1] == ".":
            dp[i][j] += dp[i][j - 1]

print(dp[H - 1][W - 1])
