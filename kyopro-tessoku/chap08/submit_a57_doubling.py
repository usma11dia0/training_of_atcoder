# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_be
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A57.py

# 教訓： doubling → 10進数→2進数化の計算を利用して、桁の繰り上がりの係数をあらかじめ計算しておくことで計算量を減らす手法

# 入力データの取得　(0-indexedで実装)
N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(0, Q)]

# 前計算(dpの導出)
LEVELS = 30
# 30の求め方
# 10**9 = 2**x から両辺に常用対数を取る
#  log10(10**9) = log10(2**x) → x = 9/log10(2) ※log10(2)=0.3より、x=30

# dp[k][i] : 2**k日後に穴iにいるとき、翌日にどの穴に移動するか
dp = [[None] * N for _ in range(0, LEVELS)]
# dpの初期値を設定
for i in range(0, N):
    dp[0][i] = A[i] - 1  # Aの各値は1-indexedであるため-1にして0-indexedに合わせる
for d in range(1, LEVELS):
    for i in range(0, N):
        dp[d][i] = dp[d - 1][dp[d - 1][i]]
        # 例：穴1にいた8日後(2**3)の場所dp[3][1]を求める時
        #   1. 穴1にいた4日後(2**2)の場所dp[2][1]を求める
        #   2. dp[2][1]の場所から4日後の場所を求めると、求めたい8日後の場所になる。
        #      よってdp[3][1] = dp[2][dp[2][1]]


# クエリの処理
for X, Y in queries:
    current_place = X - 1  # 0-indexedのため一つ減らす
    for d in range(29, -1, -1):
        # Yを2進数表記し、d桁分右にずらす。すらした後の値(2進数)に0が含まれていればFalse,そうでなければTrue
        # シフト演算する → 2倍 or 1/2倍するを意味するため、dを減らすごとに(2)**dの割り算を行っている。
        # 二進数表記で1 or 0の係数が付くかどうかの判断→(2)**dで割った時の余りが1 or 0 →　商が偶数なら余り0,奇数なら余り1
        # 商の偶奇を調べるには、1とのANDビット演算を利用する(1の桁数は商の桁数に自動で合わせられる)
        # 商の1桁目に0が入っていたら偶数、1であれば奇数
        # (Y // (2 ** d)) % 2 と実行結果は同様になる
        if ((Y >> d) & 1) == 1:
            current_place = dp[d][current_place]
    print(current_place + 1)
