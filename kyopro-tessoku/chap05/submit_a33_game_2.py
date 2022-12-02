# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ag
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap05/answer_A33.py

# 教訓：pythonでは ^ 演算子は排他的論理和の計算を実施する。
#       排他的論理和の解釈
#       ①ビットごとの排他的論理和を計算している。
#       ②排他的論理和は2値変換をして桁の繰り上がりを無視した計算結果となる。
#       ③各桁における1の個数が奇数であれば1, 偶数であれば0。


# 入力データの取得
N = int(input())
A = list(map(int, input().split()))

# ニム和を初期化
XOR_SUM = 0

# 勝者を導出する
for i in range(0, N):
    # ニム和の導出
    XOR_SUM = XOR_SUM ^ A[i]

if XOR_SUM >= 1:
    print("First")
else:
    print("Second")
