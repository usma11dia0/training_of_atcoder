# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_af
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap05/answer_A32.py

# 教訓：空配列の要素数は,0を必ず含む点に注意。


# 入力データの取得
N, A, B = map(int, input().split())

# dp[i] = 先手が勝つ状況であればTrue, 後手が勝つ状況であればFalse
# iは石の個数
dp = [None] * (N + 1)

for i in range(0, N + 1):
    if i < A and i < B:
        dp[i] = False
    elif dp[i - A] == False:
        dp[i] = True
    elif dp[i - B] == False:
        dp[i] = True
    else:
        dp[i] = False

if dp[N] == True:
    print("First")
else:
    print("Second")
