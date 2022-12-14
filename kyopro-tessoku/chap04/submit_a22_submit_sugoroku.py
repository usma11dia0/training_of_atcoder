# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_v
# answer

# 教訓 貰う遷移方式と配る遷移方式の違い？
# 配る遷移方式の場合、場合分けせずに起こりうるケースを全て記述し、大きい方 or 小さい方の値を確定とする。
# 0による初期化が原因でエラーになる事がある。(WA)で出力される。


# 入力データ
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# OK
dp = [-(10**9)] * (N + 1)
dp[1] = 0

# NG
dp = [0] * (N + 1)

# dpを用いる
for i in range(1, N):
    # マスA_iに進んだ場合
    dp[A[i - 1]] = max(dp[A[i - 1]], dp[i] + 100)
    # マスB_iに進んだ場合
    dp[B[i - 1]] = max(dp[B[i - 1]], dp[i] + 150)

print(dp[N])
