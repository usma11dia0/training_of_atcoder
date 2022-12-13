# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bd
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A56.py

# ハッシュ化を用いず配列のスライスを用いた場合(TLEで不正解)

# 入力データの取得
N, Q = map(int, input().split())
S = str(input())

a = [None] * (Q + 1)
b = [None] * (Q + 1)
c = [None] * (Q + 1)
d = [None] * (Q + 1)

for i in range(1, Q + 1):
    a[i], b[i], c[i], d[i] = map(int, input().split())

for i in range(1, Q + 1):
    if S[a[i] - 1 : b[i]] == S[c[i] - 1 : d[i]]:
        print("Yes")
    else:
        print("No")
