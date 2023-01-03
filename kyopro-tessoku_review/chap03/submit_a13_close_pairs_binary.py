# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m
# answer

# 教訓：二分探索はK以上かどうかを判定
# Leftをmid-1して調整している。→ 二分探索ではleftは必ずmid + 1。mid-1ではleft=rightが満たされない。

# 参考文献 python.bisectをスクラッチから実装
# https://qiita.com/xu1718191411/items/42f6b32959be58458546

# 入力データの取得
N, K = map(int, input().split())
A = list(map(int, input().split()))  # 0-indexed

# A[mid] - A　<= K がTrueかどうかを判定
# → Trueだった場合、答えはmid～rightの間
# → Falseだった場合、答えはleft～mid-1の間
def binary_search(mid: int, A: list, K: int, index: int) -> bool:
    if A[mid] - A[index] <= K:
        return True
    else:
        return False


cnt = 0
for i in range(0, N - 1):
    left = 0
    right = N - 1
    while left <= right:
        if left == right:
            break
        mid = (left + right) // 2
        if binary_search(mid, A, K, i):
            left = mid + 1
        else:
            right = mid
    cnt += (left) - (i + 1)


print(cnt)
# left = 1, right = 2, mid = 1, index = 0
# A[mid]=12, A[index]=11
