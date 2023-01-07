# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap03/answer_A11.py

# 二分探索の関数を定義
# 要素A[mid]の値が要素A[i]の値よりも小さければTrue,大きければFalseを返す。
def is_low(mid: int, X: int, A: list) -> bool:
    if A[mid] <= X:
        return True
    else:
        return False


# 入力データの取得
N, X = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索の初期値を設定 ※ok, ngは共にインデックス番号を示す
ok = -1
ng = len(A)

# 二分探索の実施
while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_low(mid, X, A):
        ok = mid
    else:
        ng = mid

print(ok + 1)
