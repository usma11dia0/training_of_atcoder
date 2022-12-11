# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_az
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A52.py

# 教訓：pythonの場合、stackとquereは同じdeque()で実装可能。
#       deque()はリストと同じようにデータを格納する。→先頭から順に新しいデータが格納されていく。

from collections import deque

# 入力データの取得
Q = int(input())
queries = [input().split() for i in range(0, Q)]

# クエリの処理
Queue = deque()
for q in queries:
    if q[0] == "1":
        Queue.append(q[1])
    elif q[0] == "2":
        print(Queue[0])
    elif q[0] == "3":
        Queue.popleft()
