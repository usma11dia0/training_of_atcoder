# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_e
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A05.py

# 数値の取得
N, K = map(int, input().split())

ans = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        c = K - a - b
        if 1 <= c and c <= N:
            ans += 1

print(ans)
