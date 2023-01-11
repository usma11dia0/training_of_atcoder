# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_q
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A17.py

# 教訓　部屋番号とインデックスを一致させるためには要素数+1にする


# 入力データの取得
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 貰うDPより最短経路を導出
# dp[i]: 部屋1から部屋iへ向かう最短時間
dp = [0] * (N + 1)

# 初期値の設定
dp[0] = 0
dp[1] = 0
dp[2] = A[0]

for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + A[i - 2], dp[i - 2] + B[i - 3])

# dpより逆算で経路を導出する
place = N
ans = []

while place >= 1:
    ans.append(place)
    if dp[place] - dp[place - 1] == A[place - 2]:
        place -= 1
    else:
        place -= 2

ans.reverse()

# ansの要素をそれぞれstr型へ変換
ans_str = [str(i) for i in ans]
print(len(ans_str))
print(" ".join(ans_str))
