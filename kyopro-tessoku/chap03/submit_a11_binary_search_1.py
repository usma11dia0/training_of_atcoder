# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap03/answer_A11.py

# 教訓 式の()による計算順序に注意する。
#      条件式の=有無について確認を忘れない。

# 入力データ取得
n, x = map(int, input().split())
a = list(map(int, input().split()))

# 二分探索の実施
l = 0
r = n
while l <= r:
    pivot_index = (l + r) // 2  # 小数点以下切り捨て
    if x == a[pivot_index]:
        print(pivot_index + 1)
        break
    elif x < a[pivot_index]:
        r = pivot_index - 1
    else:
        l = pivot_index + 1
