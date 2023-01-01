# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m
# answer

# 教訓：二分探索はK以上かどうかを判定
# ※※下記のコードでなぜleft == rightの条件が満たされないか分からない
# 二分探索の条件を <=K以下かどうかの判定としている。
# Leftをmid-1して調整している。

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


left = 0
right = N - 1
index = 0
while left <= right:
    print("test")
    if left == right:
        print(left)
        break
    mid = (left + right) // 2
    if binary_search(mid, A, K, index):
        # left = mid  ※収束しない
        left = mid + 1
    else:
        # right = mid -1 ※収束しない
        right = mid

# left = 1, right = 2, mid = 1, index = 0
# A[mid]=12, A[index]=11
