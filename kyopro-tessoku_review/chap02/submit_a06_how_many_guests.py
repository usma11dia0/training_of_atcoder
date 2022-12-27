# question https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap02/answer_A06.py

# 数値の取得
N, Q = map(int, input().split())
A = list(map(int, input().split()))

L = [None] * (Q + 1)
R = [None] * (Q + 1)
for i in range(1, Q + 1):
    L[i], R[i] = map(int, input().split())

# A_iの累積和リストを導出
accu_A = [0]  # 0-indexedのため0番目の要素を追加
accu = 0
for a in A:
    accu += a
    accu_A.append(accu)

# Q個の質問に回答する
for i in range(1, Q + 1):
    ans = accu_A[R[i]] - accu_A[L[i] - 1]
    print(ans)
