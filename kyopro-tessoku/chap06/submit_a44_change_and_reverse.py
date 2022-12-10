# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ar
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap06/answer_A44.py

# 教訓：反転後の要素を指定する際、わざわざ反転させなくても式変形で指定することが出来る。
#      'int' object is not subscriptable → 配列の添え字に問題がある場合が多い。

# 入力データ取得
N, Q = map(int, input().split())
Query = []
for i in range(0, Q):
    tmp = list(map(int, input().split()))
    Query.append(tmp)

# 配列Aの生成
A = [_ for _ in range(1, N + 1)]

# 反転の状態を示すフラグ
isReverse = False

for i in range(0, Q):
    if Query[i][0] == 1:
        if isReverse == False:
            A[Query[i][1] - 1] = Query[i][2]
        else:  # 逆順の場合
            A[N - Query[i][1]] = Query[i][2]
    elif Query[i][0] == 2:
        isReverse = not isReverse  # Toggleの表現
    elif Query[i][0] == 3:
        if isReverse == False:
            print(A[Query[i][1] - 1])
        else:  # 逆順の場合
            print(A[N - Query[i][1]])
