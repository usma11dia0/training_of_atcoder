# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_e
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A05.py

# 数値の取得
n, k = map(int, input().split())

# カウンター
cnt = 0

for red in range(1, n + 1):
    for blue in range(1, n + 1):
        white = k - red - blue
        if 1 <= white and white <= n:
            cnt += 1

print(cnt)
