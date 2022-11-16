# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_j
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap02/answer_A10.py

# 教訓
# 先に累積和を全て求めてしまう事で、for文の二重ループを防ぐ
# rangeのindex等には要注意

# 入力データ取得
n = int(input())
a = list(map(int, input().split()))
d = int(input())
L = [None] * d
R = [None] * d
for i in range(0, d):
    L[i], R[i] = map(int, input().split())

# 累積最大数リスト
p = [0] * n
q = [0] * n

# 1号室からn号室までの累積最大数を求める。(p)
for i in range(0, n, 1):
    if i == 0:
        p[i] = a[i]
    else:
        p[i] = max(a[i], p[i - 1])

# n号室から1号室までの累積最大数を求める。(q)
for i in range(n - 1, -1, -1):
    if i == n - 1:
        q[i] = a[i]
    else:
        q[i] = max(a[i], q[i + 1])

# L,Rの値に応じて、結果を出力する。
for i in range(0, d):
    print(max(p[(L[i] - 1) - 1], q[(R[i] + 1) - 1]))
