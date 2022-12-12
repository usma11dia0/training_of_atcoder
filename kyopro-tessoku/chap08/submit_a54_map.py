# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bb
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A54.py

# 教訓：連想配列とは”添え字の制限がない配列"
#       Pythonでは連想配列=Dictionary

# 入力データの取得
Q = int(input())
Queries = [input().split() for _ in range(0, Q)]

# クエリの処理
Map = {}
for q in Queries:
    if q[0] == "1":
        Map[q[1]] = q[2]
    elif q[0] == "2":
        print(Map[q[1]])
