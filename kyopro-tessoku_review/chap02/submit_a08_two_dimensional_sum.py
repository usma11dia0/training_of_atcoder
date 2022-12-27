# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap02/answer_A08.py

# 二次元累積和がなぜ成り立つかについては、p63の注釈※4を要参照。(横方向だけの累積和を一旦考える)
# 二次元累積和の理想的なデータの持ち方は？ →　行ごとにリストが格納された二次元配列
# →List[][]この形で要素を取り出せる → 行方向・列方向のループに強い

# 二次元配列の作成方法
# ポイント 初めにn*wの空行列を作成する。
# (行列ともに+1するのが重要。n,wが1の時のエッジケース対策になる。)

# 入力値の取得
H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(0, H)]
Q = int(input())
A = [0] * (Q + 1)
B = [0] * (Q + 1)
C = [0] * (Q + 1)
D = [0] * (Q + 1)
for i in range(1, Q + 1):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# Xの横方向の累積和リストを導出
X_accu_row = []

# 行方向に繰り返し
for i in range(0, H):
    accu_row = 0
    list_accu_row = []
    # 列方向に累積
    for j in range(0, W):
        accu_row += X[i][j]
        list_accu_row.append(accu_row)
    X_accu_row.append(list_accu_row)

print(X)
print(X_accu_row)
