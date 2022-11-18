# question https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap03/answer_A14.py
# answer

# 教訓 配列内に要素があるかないかを判定するのにも二分探索が利用できる。

import bisect
import sys

# 入力データ取得
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

# p,q配列を準備
p = [] * n**2
for i in range(0, n):
    for j in range(0, n):
        p.append(a[i] + b[j])

q = [] * n**2
for i in range(0, n):
    for j in range(0, n):
        q.append(c[i] + d[j])

# 配列qをソート
q.sort()

# 二分探索
# p + q = k ≒ q = k - p_n**2 を満たすqが存在するかを調べる
for i in range(0, n**2):
    p_n_n = p[i]
    tg = k - p_n_n
    tg_index = bisect.bisect_left(q, tg)  # tgが挿入可能な要素番号
    # tgがq内にあれば、qのtg_index番はtgになる。
    # tgが最大値になる場合は要素数+1を返すため、tg_indexが要素数を超える際もFalse判定する。
    if tg_index < n**2 and q[tg_index] == tg:
        print("Yes")
        sys.exit(0)

print("No")
