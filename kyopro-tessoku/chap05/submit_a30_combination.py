# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ad
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap05/answer_A30.py

# 教訓：関数名は頭文字を大文字にする

# 入力データの取得
n, r = map(int, input().split())
M = 1000000007

# 関数定義
# a^bをmで割った余りを返す関数 (繰り返し二乗法を利用)
def Power(a: int, b: int, m: int) -> int:
    p = a
    answer = 1
    # bを二値変換する
    for i in range(0, 30):
        wari = 2**i
        if (b // wari) % 2:
            answer = (answer * p) % m
        p = (p * p) % m
    return answer


# a÷bをmで割った余りを返す関数
# ≒a*b^(m-2)をmで割った余りを返す関数
def Division(a, b, m):
    return (a * Power(b, m - 2, m)) % m


# 手順1 分子(n!)を求める
a = 1
for i in range(1, n + 1):
    a = (a * i) % M

# 手順2 分母(r!×(n-r)!)を求める
b = 1
for i in range(1, r + 1):
    b = (b * i) % M
for i in range(1, n - r + 1):
    b = (b * i) % M

# 手順3 答えを導出する
ans = Division(a, b, M)
print(ans)
