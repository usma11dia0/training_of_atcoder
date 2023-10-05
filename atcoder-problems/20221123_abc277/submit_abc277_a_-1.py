# question https://atcoder.jp/contests/abc277/tasks/abc277_a

import sys

# 入力データ
n, x = map(int, input().split())
p = list(map(int, input().split()))

for i in range(0, n):
    if p[i] == x:
        print(i + 1)
        sys.exit(0)
