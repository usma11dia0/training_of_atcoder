# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ab
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap05/answer_A28.py

# 教訓： 配列内の型変換は内包表記かmapを用いる。

# 入力データの取得
N = int(input())
T = [None] * N
A = [None] * N

for i in range(0, N):
    T[i], A[i] = map(str, input().split())
A = [int(str) for str in A]

# 参考:回答の書き方
# for i in range(N):
# 	T[i], A[i] = input().split()
# 	A[i] = int(A[i])

ans = 0
for i in range(0, N):
    if T[i] == "+":
        ans = ans + A[i]
    elif T[i] == "*":
        ans = ans * A[i]
    elif T[i] == "-":
        ans = ans - A[i]

    ans = ans % 10000
    print(ans)

    if ans < 10000:
        ans += 10000
