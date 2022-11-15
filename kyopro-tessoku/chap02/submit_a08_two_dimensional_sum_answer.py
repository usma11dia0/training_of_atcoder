# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap02/answer_A08.py


# 入力値の取得
h, w = map(int, input().split())
x_matrix = [list(map(int, input().split())) for j in range(0, h)]
q = int(input())
a_matrix = [list(map(int, input().split())) for j in range(0, q)]

# ポイント 初めにn*wの空行列を作成する。
# (行列ともに+1するのが重要。n,wが1の時のエッジケース対策になる。)
accu_matrix = [[0] * (w + 1) for i in range(0, h + 1)]

# 行方向の累積和行列を導出する
for i in range(1, h + 1):
    for j in range(1, w + 1):
        accu_matrix[i][j] = accu_matrix[i][j - 1] + x_matrix[i - 1][j - 1]

# 列方向の累積和行列を導出する
for j in range(1, w + 1):
    for i in range(1, h + 1):
        accu_matrix[i][j] = accu_matrix[i - 1][j] + accu_matrix[i][j]

# 各質問の答えを導出する
for a in a_matrix:
    ans = 0
    ans = (
        accu_matrix[a[2]][a[3]]
        - accu_matrix[a[0] - 1][a[3]]
        - accu_matrix[a[2]][a[1] - 1]
        + accu_matrix[a[0] - 1][a[1] - 1]
    )
    print(ans)
