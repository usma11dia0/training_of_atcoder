# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_aq
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap06/answer_A43.py

# 教訓：

# 入力データ取得
N, L = map(int, input().split())
A = [None] * (N + 1)
B = [None] * (N + 1)

for i in range(1, N + 1):
    A[i], B[i] = input().split()  # 一旦文字列で格納
    A[i] = int(A[i])  # Aの配列要素をint化

# 人iが歩く速度
speed = 1

ans = 0
for i in range(1, N + 1):
    if B[i] == "E":
        arrive_time = (L - A[i]) // speed
    else:
        arrive_time = A[i] // speed

    ans = max(ans, arrive_time)

print(ans)
