# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_d
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A04.py

# 数値の取得
N = int(input())

digit = 10
ans = ""
for i in range(digit - 1, -1, -1):
    binary = (N // 2**i) % 2
    ans += str(binary)
    if binary == 1:
        N -= 2**i

print(ans)
