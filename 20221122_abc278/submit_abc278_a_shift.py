# question https://atcoder.jp/contests/abc278/tasks/abc278_a

# 入力データ
n, k = map(int, input().split())
a = list(map(int, input().split()))

a = a[k:]
for i in range(1, k + 1):
    if i > n:
        break
    a.append(0)

for ans in a:
    print(ans, end=" ")
