# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m
# answer

# 入力
n, k = map(int, input().split())
a = list(map(int, input().split()))

# 配列の準備
# a[r] - a[i] >= kとなる最小のインデックスrを格納する配列
r = [None] * n

# しゃくとり法
for i in range(0, n - 1):
    # スタート地点を決める
    if i == 0:
        r[i] = 0
    else:
        r[i] = r[i - 1]

    # ギリギリまで増やしていく
    while r[i] < n - 1 and a[r[i] + 1] - a[i] <= k:
        r[i] += 1

# 出力
Answer = 0
for i in range(0, n - 1):
    Answer += r[i] - i
print(Answer)
