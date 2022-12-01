# question https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_aq
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap05/answer_A29.py

# 教訓：10^9 = 2^30の30の求め方
# 10^9 = 2^iとする。両辺にlog10を取ると、
# log10(10)^9 = log10(2)^i
# 9 = i * log10(2)
# 9 / log10(2) = i
# ここで、log10(2)=0.3なので、
# i = 9 / 0.3 = 30

# 入力データの取得

# a の b 乗を m で割った余りを返す関数
def Power(a, b, m):
    p = a
    Answer = 1
    for i in range(30):
        wari = 2**i
        # bを二進数表記
        if (b // wari) % 2 == 1:
            # bを二進数表記して1になった場合、
            Answer = (Answer * p) % m  # a の 2^i 乗が掛けられるとき
            # 掛け算の場合は余りをいつ計算しても良いため、計算の都度余りを導出する。
        p = (p * p) % m  # p=aの2^iを示している。
    return Answer


# 入力
a, b = map(int, input().split())

# 出力
print(Power(a, b, 1000000007))
