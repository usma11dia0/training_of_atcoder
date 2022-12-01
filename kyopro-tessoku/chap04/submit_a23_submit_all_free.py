# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_w
# answer

# 教訓
# 配る遷移方式の場合、場合分けせずに起こりうるケースを全て記述し、大きい方 or 小さい方の値を確定とする。

# 配る遷移方式であるため、dp[i-1][S]を指す状態からの遷移をすべて列挙。
# dp[i][j] = min(dp[i][j], dp[i-1][j]) ※クーポン券iを用いない場合  dp[i][j]はdp[i][v]によって更新される場合があるため、現在のdp[i][j]との比較をする。
# dp[i][v] = min(dp[i][v], dp[i-1][j] + 1) ※クーポン券iを用いる場合

# 配列の初期化
# 主にDPで用いる？　動作しない値の対処。
# 最小値を求める際に空欄の値は最大(inf)、
# 逆に最大値を求める際は空欄の値を最小(-inf)にしておく


# 入力データ
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(0, M)]

# 配列の初期化
dp = [[10**9] * (2**N) for i in range(0, M + 1)]

# 動的計画法
dp[0][0] = 0
for i in range(1, M + 1):
    # jはビットの数列を示す数値。二値変換された値は品物の集合を示す。
    for j in range(0, 2**N):
        # alreadyはjの二値変換後の値を格納した配列。already[k] = 1 のとき、品物kは既に無料になっている
        already = [None] * N
        # jの値を二値変換
        for k in range(0, N):
            if (j // (2**k)) % 2 == 0:  # 割り算の図の逆をイメージ。上から順に2^kの割り算をしている。
                already[k] = 0
            else:
                already[k] = 1
        # クーポンiを選んだ場合の整数表現vを計算する (SとTの和集合)
        v = 0
        for k in range(0, N):
            if already[k] == 1 or A[i - 1][k] == 1:
                v += 2**k

        # 遷移を行う
        dp[i][j] = min(dp[i][j], dp[i - 1][j])  # クーポンiを用いなかった場合
        dp[i][v] = min(dp[i][v], dp[i - 1][j] + 1)  # クーポンiを用いた場合

# 出力
if dp[M][2**N - 1] == 10**9:
    print("-1")
else:
    print(dp[M][2**N - 1])
