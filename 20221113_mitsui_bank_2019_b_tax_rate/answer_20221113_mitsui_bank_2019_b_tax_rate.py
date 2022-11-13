# question https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b
# 解説資料 https://img.atcoder.jp/sumitrust2019/editorial.pdf

import math

# 数値の取得
n = int(input())

# 税率
tax_rate = 1.08

tmp = math.ceil(n / tax_rate)
print(f"ceil適用前 {n / tax_rate}")
print(f"ceil適用後 {tmp}")

if math.floor(tmp * tax_rate) == n:
    ans = tmp
    print(tmp)
else:
    print(":(")
