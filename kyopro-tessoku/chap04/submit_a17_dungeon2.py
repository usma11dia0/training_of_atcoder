# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_q
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A17.py

# 教訓　部屋番号とインデックスを一致させるためには要素数+1にする

# 入力データ取得
n = int(input())
a = list(map(int, input().split()))  # iは2～nまで
b = list(map(int, input().split()))  # iは3～nまで

# DPで部屋1～部屋Nまでの最短時間を導出する (index = 0が含まれるため+1)
dp = [0] * (n + 1)

# 初期値を設定
# 部屋0は存在しないため0
dp[0] = 0

# 部屋1へ向かう最短移動時間
dp[1] = 0

# 部屋2へ向かう最短移動時間
dp[2] = a[0]

# DPの実装
for i in range(3, n + 1):
    # 一つ先の部屋へ移動の場合
    a_tmp = dp[i - 1] + a[i - 2]
    # 二つ先の部屋へ移動の場合
    b_tmp = dp[i - 2] + b[i - 3]
    # dp[i]の値はa_tmp or b_tmpの小さい方
    dp[i] = min(a_tmp, b_tmp)

# ゴールから逆算して最短経路を導出
place = n
ans = []
while place >= 1:
    ans.append(place)
    if dp[place] - dp[place - 1] == a[place - 2]:
        place = place - 1
    else:
        place = place - 2

# 結果を出力
ans.reverse()
ans2 = [str(s) for s in ans]
print(len(ans2))
print(" ".join(ans2))
