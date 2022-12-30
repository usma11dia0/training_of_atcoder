# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap03/answer_A11.py

# 教訓 式の()による計算順序に注意する。
#      条件式の=有無について確認を忘れない。

# 入力データ取得
N, X = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索法を実装
l = 0
r = N
while l <= r:
    # 中間要素の値を取得
    pivot_index = (l + r) // 2

    # 対象Xが見つかった場合
    if A[pivot_index] == X:
        print(pivot_index + 1)
        break
    # 対象Xが中間の要素よりも小さい場合
    elif X < A[pivot_index]:
        r = pivot_index - 1
    # 対象Xが中間の要素よりも大きい場合
    elif A[pivot_index] < X:
        l = pivot_index + 1
