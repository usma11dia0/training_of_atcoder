# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_i
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap02/answer_A09.py

# 教訓：# +1 のみでは index -1対策や0-indexed対策にはなるものの、index+1の対策にはならない。→ +2必要

# 入力データの取得
H, W, N = map(int, input().split())
A = [0] * (N + 1)
B = [0] * (N + 1)
C = [0] * (N + 1)
D = [0] * (N + 1)

for i in range(1, N + 1):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# 累積和行列を初期化する
accu_matrix = [[0] * (W + 2) for _ in range(0, H + 2)]  # indexが+1されているため、要素数+1の行列が必要。


# 積雪する長方形領域を取得
for i in range(1, N + 1):
    accu_matrix[A[i]][B[i]] += 1
    accu_matrix[C[i] + 1][D[i] + 1] += 1
    accu_matrix[A[i]][D[i] + 1] -= 1
    accu_matrix[C[i] + 1][B[i]] -= 1

# 累積和行列の作成(積雪量の導出)
# 横方向に累積和を求める
for i in range(1, H + 1):
    for j in range(1, W + 1):
        accu_matrix[i][j] = accu_matrix[i][j - 1] + accu_matrix[i][j]

# 縦方向に累積和を求める
for j in range(1, W + 1):
    for i in range(1, H + 1):
        accu_matrix[i][j] = accu_matrix[i - 1][j] + accu_matrix[i][j]

# 結果を出力する
for i in range(1, H + 1):
    for j in range(1, W + 1):
        print(accu_matrix[i][j], end=" ")
    print()
