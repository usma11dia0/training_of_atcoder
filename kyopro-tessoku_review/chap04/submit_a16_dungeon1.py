# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A16.py

# 教訓 DPの基本的な考え方 「小さい問題の結果」から計算する手法
# 【貰うDP】：マス (i,j) へと至るまでの直前の行動で場合分け。dp[]の値が確定する。
# 【配るDP】：マス (i,j) へと至るまでの直後の行動で場合分け。dp[]の値が暫定的であり更新される可能性がある。

#  DPを考える際は初期値に注意する。

# 参考資料：https://algo-method.com/descriptions/78

# 入力データの取得
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 動的計画法の実装
dp = [0] * (N + 1)

# 貰うDP
# 部屋i-1 → 部屋iの経路で部屋iへ向かう
for i in range(2, N + 1):
    if i == 1:
        dp[i] = 0
    elif i == 2:
        dp[i] = A[i - 2]  # Aは0-indexedである点に注意
    else:
        dp[i] += min(dp[i - 1] + A[i - 2], dp[i - 2] + B[i - 3])
print(dp[N])


# 配るDP
# 入力（A, B が 0 番目から始まっていることに注意）
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 配列 dp の初期化
dp = [2000000000] * N
dp[0] = 0

# 動的計画法
for i in range(N):
    if i <= N - 2:
        dp[i + 1] = min(dp[i + 1], dp[i] + A[i])
    if i <= N - 3:
        dp[i + 2] = min(dp[i + 2], dp[i] + B[i])

# 出力
print(dp[N - 1])
