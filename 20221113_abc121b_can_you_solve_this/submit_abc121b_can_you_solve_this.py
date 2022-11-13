# question https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

# 数値の取得
n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = []
for i in range(0, n):
    a_row = list(map(int, input().split()))
    a.append(a_row)

# 外生変数
counter = 0

# 条件記載
for i in range(0, n):
    sum = 0
    for j in range(0, m):
        sum += a[i][j] * b[j]
    if sum + c > 0:
        counter += 1

print(counter)
