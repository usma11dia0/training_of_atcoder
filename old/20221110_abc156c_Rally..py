# question https://atcoder.jp/contests/abc156/tasks/abc156_c
# 解説動画(26分前後) https://www.youtube.com/watch?v=lzAMKPMLdtU

# # # テスト用
# a = 20
# b = 1

# 数値の取得
n = int(input())
xi = list(map(int, input().split()))

# 回答1 総当たり
# Xiの最小値～最大値までをすべて試して、最小値を答えとする。
mi = min(xi)
ma = max(xi)
ans = 10000000
for i in range(mi, ma + 1):
    num = 0
    for j in range(n):
        num += (xi[j] - i) ** 2
    ans = min(ans, num)
print(ans)
