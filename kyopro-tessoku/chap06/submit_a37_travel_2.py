# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ak
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap06/answer_A37.py

# 教訓：主客転倒テクニックの本質は、「問題を複数のパーツに分解し、各パーツの”答えへの寄与分”を求める手法」

# 入力データ取得
N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

# 主客転倒テクニックを用いる
A_SUM = 0
for a in A:
    A_SUM += a

C_SUM = 0
for c in C:
    C_SUM += c

ans = 0
ans = A_SUM * M + B * (N * M) + C_SUM * N
print(ans)
