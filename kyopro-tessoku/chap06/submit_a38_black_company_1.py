# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_al
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap06/answer_A38.py

# 教訓：上限値にて配列の初期化を行う

# 入力データ取得
D, N = map(int, input().split())
L = [None] * (N + 1)
R = [None] * (N + 1)
H = [None] * (N + 1)

for i in range(1, N + 1):
    L[i], R[i], H[i] = map(int, input().split())

# 上限値にて配列を初期化(24h)
# LIM[i]:i日目における最大の労働時間
LIM = [24] * (D + 1)

for i in range(1, N + 1):
    for j in range(L[i], R[i] + 1):  # 条件iの日付の範囲
        LIM[j] = min(LIM[j], H[i])

# 答えの導出
ans = 0
for i in range(1, D + 1):
    ans += LIM[i]

print(ans)
