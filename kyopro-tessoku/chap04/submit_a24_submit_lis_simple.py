# question
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A24.py

# 教訓 通常のDPを行った場合の回答(TLEとなってしまう)

# 入力データ取得
N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)  # 先頭に0を追加


# dp[i] = 最後の要素がAiである部分列のうち、最長のものの長さ
dp = [-10 ^ 5] * (N + 1)
dp[1] = 1
for i in range(1, N + 1):
    dp[i] = 1
    for j in range(1, i, 1):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

ans = 0
for i in range(1, N + 1):
    ans = max(ans, dp[i])
print(ans)
