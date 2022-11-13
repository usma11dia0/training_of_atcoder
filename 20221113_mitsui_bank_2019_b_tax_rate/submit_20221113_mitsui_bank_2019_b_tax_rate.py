# question https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

# import math

# 数値の取得
n = int(input())

# 税率
tax_rate = 1.08

tmp = round(n % tax_rate)
print(f"round適用前 {n % tax_rate}")
print(f"round適用後 {tmp}")

if round(n % tax_rate) == 1:
    ans = n / tax_rate
    print(round(ans))
else:
    print(":(")
