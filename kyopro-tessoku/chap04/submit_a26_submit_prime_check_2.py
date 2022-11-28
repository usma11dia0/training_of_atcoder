# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_z
# answer

# 教訓：すべての合成数は2以上√x以下の約数を持つことを利用する。
#       よく用いる処理は関数化して再利用性を高める。

import sys

# 入力データの取得
Q = int(input())
X = [int(input()) for _ in range(0, Q)]


def isPrime(num: int) -> bool:
    prime_flag = True
    LIMIT = int(num**0.5)
    for i in range(2, LIMIT + 1):
        if (num % i * i) == 0:
            prime_flag = False
            return prime_flag
    return prime_flag


for x in X:
    if isPrime(x) == True:
        print("Yes")
    else:
        print("No")
