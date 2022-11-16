# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap02/answer_A08.py

# 教訓
# 下記方法だと、行列を入れ替える必要あり → 手間がかかる。初めに要素h*wの空行列を作成した方が楽

# 入力値の取得
h, w = map(int, input().split())
x_matrix = [list(map(int, input().split())) for j in range(0, w)]
q = int(input())
a_matrix = [list(map(int, input().split())) for j in range(0, q)]


# 累積和行列を求める
# x軸方向の累積和行列
accu_x_matrix = []
for i in range(0, h):
    accu = 0
    accu_list = []
    for j in range(0, w):
        accu += x_matrix[i][j]
        accu_list.append(accu)
    accu_x_matrix.append(accu_list)

# x + y軸方向の累積和行列
accu_matrix = []
for j in range(0, w):
    accu = 0
    accu_list = []
    for i in range(0, h):
        accu += accu_x_matrix[i][j]
        accu_list.append(accu)
    accu_matrix.append(accu_list)
    # 行列を入れ替える必要あり → 手間がかかる。初めに要素h*wの空行列を作成した方が楽

print(accu_x_matrix)
print(accu_matrix)


# リスト内包表記を用いない場合
# x_matrix = []
# for j in range(0, w):
#     x = list(map(int, input().split()))
#     x_matrix.append(x)
# print(x_matrix)

# サンプルプログラム
# z_matrix = [[0] * w for i in range(0, h)]
# print(z_matrix)

# # リスト内包表記を用いない場合
# z_matrix = []
# for row in range(0, h):
#     z = [0] * w
#     z_matrix.append(z)
# print(z_matrix)
