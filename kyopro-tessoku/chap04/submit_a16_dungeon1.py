# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A16.py

# 教訓　部屋番号とインデックスを一致させるためには要素数+1にする
#       DPを考える際は、最後の行動で場合分けすると見通しが良くなることがある。

# 入力データ取得
n = int(input())
a = list(map(int, input().split()))  # iは2～nまで
b = list(map(int, input().split()))  # iは3～nまで

# DPで導出する
dp = [0] * (n + 1)  # index 0がn含まれてしまい部屋n番目が不足してしまうため、n+1をする。
# 初期値を設定
for i in range(2, n + 1):
    # i = 0, 1の時は部屋の移動がないため0
    if i == 2:
        dp[i] = a[i - 2]
    # iが3以上の時
    else:
        # 一つ先の部屋へ移動の場合
        a_tmp = dp[i - 1] + a[i - 2]
        # 二つ先の部屋へ移動の場合
        b_tmp = dp[i - 2] + b[i - 3]
        # dp[i]の値はa_tmp or b_tmpの小さい方
        dp[i] = min(a_tmp, b_tmp)

print(dp[i])
