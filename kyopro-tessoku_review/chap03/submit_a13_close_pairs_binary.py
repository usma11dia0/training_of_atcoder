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
# → Trueだった場合、答えはmid+1～rightの間
# → Falseだった場合、答えはleft～midの間
def binary_search(mid: int, A: list, K: int, index: int) -> bool:
    if A[mid] - A[index] <= K:
        return True
    else:
        return False


# left = 6が答えになるときと, left = 7が答えになる時の違いは?

cnt = 0
for i in range(0, N - 1):
    left = 0
    right = N - 1
    while left <= right:
        # leftが末尾まで移動した場合は処理を続行 (left=right=6,mid=6を計算)
        # left = N - 1が答えの時に無限ループになる点に注意
        if left == right and left != N - 1:
            break
        mid = (left + right) // 2
        if binary_search(mid, A, K, i):
            left = mid + 1
        else:
            right = mid
            # left = N - 1が答えの時にループを抜け出すための条件
            if right == N - 1:
                break
    cnt += left - (i + 1)
print(cnt)

# left = mid, right = mid-1 だと二分探索出来ない理由
# left = 1, right = 2, mid = 1, index = 0の時、
# A[mid]=12, A[index]=11
# 二分探索条件では, A[mid] - A[index] <= 10がTrueになり、left = midの更新がなされる
# → leftが変わらず無限ループとなる

# A = [11, 12, 16, 22, 27, 28, 31]
