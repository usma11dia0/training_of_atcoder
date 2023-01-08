# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m
# answer

# 教訓：しゃくとり法の考え方の基礎は、自明な範囲の探索を再度実行しないこと

# 参考資料：https://www.akiradeveloper.com/post/syakutori/

# 入力データ取得
N, K = map(int, input().split())
A = list(map(int, input().split()))  # 0-indexed

# 尺取り法の実装

# 配列の初期化(解の格納先)
# r[i]: A[r[i]+1] - A[i] <= K を満たす最大の要素番号+1
r = [None] * N

for i in range(0, N - 1):
    # 初期値の設定
    if i == 0:
        r[i] = 0
    else:
        r[i] = r[i - 1]

    while r[i] != N - 1 and A[r[i] + 1] - A[i] <= K:
        r[i] += 1

# 結果の出力
ans = 0
for i in range(0, N - 1):
    ans += r[i] - i

print(ans)
