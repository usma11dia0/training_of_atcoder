# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_r
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A18.py

# 教訓
# 配列の[-2]など逆順参照を実行してしまわないかに留意する。
#  　(例) j = 5, Ai = a[i - 1] = 7の時
#          dp[i - 1][j - a[i - 1]] = dp[4][-2] = dp[4][5]が参照されてしまう。

# 3.4半分全列挙 four boxes(p.97)と似た問題であるが、この問題では使えない。
# 半分全列挙では最終的に要素が配列Qに存在するかどうかという二分探索問題へ落とし込むが、
# そのためには"配列Qの中に要素K-Piは存在するか"のように、Piの値を固定出来ないといけない。
# 今回の問題ではPi部分が固定されない。

# 部分和問題では、Piが変動する。
# DPで悩んだときは、最後の行動で場合分けしてみる。

import sys

# 入力データ取得
n, s = map(int, input().split())  # 共に1以上
a = list(map(int, input().split()))  # 1以上 → i-1 が要素Aiの値になる。# 例 要素0番目 →A1の値
# DPを用いて導出
dp = []
for i in range(0, n + 1):
    dp.append([0] * (s + 1))

# カード0枚,合計0は常に成立
dp[0][0] = True

for i in range(1, n + 1):  # 用いるカードの枚数
    for j in range(0, s + 1):  # 合計値

        # この場合分けはなぜ必要？ → 合計値がAiよりも低い場合でも、方法Bが該当することがある？
        # 　→配列の[-2]など逆順参照を防ぐため。
        #  　(例) j = 5, Ai = a[i - 1] = 7の時
        #          dp[i - 1][j - a[i - 1]] = dp[4][-2] = dp[4][5]が参照されてしまう。
        if j < a[i - 1]:  # 合計値がAiよりも低い場合
            if dp[i - 1][j] == True:
                dp[i][j] = True

        if a[i - 1] <= j:
            if dp[i - 1][j] == True or dp[i - 1][j - a[i - 1]] == True:
                dp[i][j] = True

# 結果を出力
if dp[n][s] == True:
    print("Yes")
else:
    print("No")
