# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_d
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A04.py

# 数値の取得
n = int(input())

# 外生変数
# 桁数
digits = 10

# 回答
ans = ""

for i in range(digits - 1, -1, -1):
    if (n // 2**i) % 2 == 1:
        ans += "1"
        n = n - 2**i
    else:
        ans += "0"

print(ans)
