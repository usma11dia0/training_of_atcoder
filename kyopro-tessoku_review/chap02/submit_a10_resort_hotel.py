# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_j
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap02/answer_A10.py

# 教訓
# 先に累積maxを全て求めてしまう事で、for文の二重ループを防ぐ
# ループ文でout of index対策として、添え字の他に初項を先に指定する方法もある。

# 手順
# 1. 出力はmax(1～l - 1の最大値, r+1～nの最大値)
# 2. 1～l-1の最大値は右からの累積maxから、r+1～nの最大値については左からの累積maxから導出する。
# 先に累積maxを計算し、そのあと要素番号で最大値を出力するため計算量を効率化出来ている。

# 入力データの取得
N = int(input())
A = list(map(int, input().split()))
D = int(input())
L = [0] * (D + 1)
R = [0] * (D + 1)
for i in range(1, D + 1):
    L[i], R[i] = map(int, input().split())

# Aの左側からの累積maxリストを作成する
A_left_accumax = [0] * (N + 1)
for i in range(1, N + 1):
    A_left_accumax[i] = max(A_left_accumax[i - 1], A[i - 1])

# Aの右側からの累積maxリストを作成する
A_right_accumax = [0] * (N + 1)
# A_left_accumaxリストの末尾に初期値を設定
A_right_accumax[N] = A[-1]
for i in range(N - 1, 0, -1):
    A_right_accumax[i] = max(A_right_accumax[i + 1], A[i - 1])

# d日目に使える最も大きい部屋を出力する
for i in range(1, D + 1):
    print(max(A_left_accumax[L[i] - 1], A_right_accumax[R[i] + 1]))
