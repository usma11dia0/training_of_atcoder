# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_i
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap02/answer_A09.py

# 教訓
# 二次元座標の入力データの取得は回答のようにそれぞれ独立させた方が良いかも

# 入力データ取得
h, w, n = map(int, input().split())

# 二次元座標データをそれぞれ独立させて取得
A = [None] * n
B = [None] * n
C = [None] * n
D = [None] * n
for i in range(0, n):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# 累積和行列の空行列を作成
# ※本問題では左下座標+1の座標を利用し、かつfor文を1スタートにするため、+2する必要がある。
accu_matrix = [[0] * (w + 2) for i in range(0, h + 2)]

# 累積和行列導出に必要な座標を特定する
for i in range(0, n):
    accu_matrix[A[i]][B[i]] += 1
    accu_matrix[C[i] + 1][D[i] + 1] += 1
    accu_matrix[A[i]][D[i] + 1] -= 1
    accu_matrix[C[i] + 1][B[i]] -= 1

# 行方向の累積和行列を導出する
for i in range(1, h + 1):
    for j in range(1, w + 1):
        accu_matrix[i][j] = accu_matrix[i][j - 1] + accu_matrix[i][j]

# 行方向＋列方向の累積和行列を導出する
for j in range(1, w + 1):
    for i in range(1, h + 1):
        accu_matrix[i][j] = accu_matrix[i - 1][j] + accu_matrix[i][j]

# 結果を出力する
for i in range(1, h + 1):
    for j in range(1, w + 1):
        # 各座標間に半角スペースを入れるために必要
        if j >= 2:
            print(" ", end="")
        print(accu_matrix[i][j], end=" ")
    print()
