# question https://atcoder.jp/contests/abc278/tasks/abc278_c

# 教訓 Nが10^9の時は二次元配列が使えない。(一次元配列でも不可能)
#      →setを用いる 集合を効率的に扱えるデータセットであるため、10^9でも扱える。

# 入力データ
N, Q = map(int, input().split())

T = [None] * (Q + 1)
A = [None] * (Q + 1)
B = [None] * (Q + 1)
for i in range(1, Q + 1):
    T[i], A[i], B[i] = map(int, input().split())

# フォロー・アンフォロー配列
follow = [[0] * (N + 1) for _ in range(0, N + 1)]

for i in range(1, Q + 1):
    if T[i] == 1:
        follow[A[i]][B[i]] = 1
    elif T[i] == 2:
        follow[A[i]][B[i]] = 0
    elif T[i] == 3:
        if follow[A[i]][B[i]] == 1 and follow[B[i]][A[i]] == 1:
            print("Yes")
        else:
            print("No")
