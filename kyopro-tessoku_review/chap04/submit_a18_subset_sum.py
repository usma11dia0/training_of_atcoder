# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_r
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A18.py

# 教訓
# boolean値が答えの時に、初期値としてFalse等入れない。　None or 0を入れる。
# DPの実装時は初期値の設定に注意する！
# DPや配列内の引き算 "j - A[i - 1]"には要注意！ －のインデックによる参照を防ぐ。
# for文の順番にも注意。Nを先にまわすかSを先にするか。

# 入力データの取得
N, S = map(int, input().split())
A = list(map(int, input().split()))

# 方針 貰うDP
# dp[i][j] : カード1～iを用いて合計jとなるカードの選び方があるか否か
# dp[i][j] がTrueとなるための条件
# 1. 1～i-1の時点で、すでにTrue →  dp[i-1][j] == True
# 2. 1～i-1の時点で、次にカードiを用いればjとなる時 →　dp[i-1][j - A_i] == True

dp = [[0] * (S + 1) for _ in range(0, N + 1)]

dp[0][0] = True

for i in range(1, N + 1):
    for j in range(0, S + 1):
        if j < A[i - 1]:
            if dp[i - 1][j] == True:
                dp[i][j] = True

        if A[i - 1] <= j:
            if (dp[i - 1][j] == True) or (dp[i - 1][j - A[i - 1]] == True):
                dp[i][j] = True

# 結果を出力
if dp[N][S] == True:
    print("Yes")
else:
    print("No")
