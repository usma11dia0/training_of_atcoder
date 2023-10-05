# question https://atcoder.jp/contests/abc277/tasks/abc277_b


# 教訓 空の集合を定義する際はset()を用いる。
# b = {} だと辞書型になってしまう。

# flagを生成して、最後に判定する方が効率的

import sys

# 入力データ
N = int(input())
S = [str(input()) for _ in range(0, N)]

cond1 = {"H", "D", "C", "S"}
cond2 = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}

str_set = set()

for s in S:
    if s[0] in cond1 and s[1] in cond2:
        if str_set == set() or s not in str_set:
            str_set.add(s)
        else:
            print("No")
            sys.exit(0)
    else:
        print("No")
        sys.exit(0)

print("Yes")
