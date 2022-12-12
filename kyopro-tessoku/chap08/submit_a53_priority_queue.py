# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ba
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A53.py

# 教訓：優先度付きキューとは、キューの中の最小の要素を扱うことが出来るデータ構造
# 注意 1：Python の heapq モジュールは、deque モジュールとは異なり、関数を使って list を操作するという形式になっています。
# 注意 2：優先度付きキューの最小要素は T[0] で取り出せますが、例えば小さいほうから 2 番目の要素が T[1] で取り出せるとは限らないことに注意してください。

import heapq

# 入力データの取得
Q = int(input())
Queries = [list(map(int, input().split())) for _ in range(0, Q)]

# クエリの処理
T = []
for q in Queries:
    if q[0] == 1:
        heapq.heappush(T, int(q[1]))
    elif q[0] == 2:
        print(T[0])
    elif q[0] == 3:
        heapq.heappop(T)
