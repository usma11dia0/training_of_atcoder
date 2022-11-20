# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_s
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A19.py

# 教訓

# DPはビット全探索の応用のようなイメージ

# 動的計画法が使えるかどうかの見極め方
# A. 数ある選択肢の中で最適解を求める際に利用？
# 一次元配列か二次元配列か?
# A. dp[i]の場合分けを行う際に、情報が足りないとき、添え字を付け加え二次元配列にする。
# https://qiita.com/drken/items/a5e6fe22863b7992efdb  ※問題2 ナップサック問題参照


# 入力データ取得
N, W = map(int, input().split())  # 　1<=i

w = [None] * (N)  # 要素0がindex 1の値
v = [None] * (N)  # 要素0がindex 1の値

for i in range(0, N):
    w[i], v[i] = map(int, input().split())

# DP法を用いる
# 空の配列
dp = [[0] * (W + 1) for _ in range(0, N + 1)]

for i in range(1, N + 1):
    for j in range(1, W + 1):
        i_choice = no_choice = 0
        if 0 <= j - w[i - 1] and j - w[i - 1] <= W:
            # 品物iを選んだ場合
            i_choice = dp[i - 1][j - w[i - 1]] + v[i - 1]
        # 品物iを選ばなかった場合
        if 0 <= j:
            no_choice = dp[i - 1][j]
        dp[i][j] = max(i_choice, no_choice)

# 結果の出力
ans = 0
for j in range(1, W + 1):
    tmp = dp[N][j]
    ans = max(ans, tmp)
print(ans)
