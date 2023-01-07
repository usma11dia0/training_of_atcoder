# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m
# answer

# 教訓：二分探索実装時には配列外参照にも気を配る
#      left,rightを用いるのではなく、okとngに分けて考えると分かりやすい

# 参考文献
# めぐる式二分探索
# https://www.forcia.com/blog/001434.html

# 二分探索用の関数を定義
def is_ok(mid: int, i: int, K: int, A: list) -> bool:
    if A[mid] - A[i] <= K:
        return True
    else:
        return False


# 入力データの取得
N, K = map(int, input().split())
A = list(map(int, input().split()))  # 0-indexed

# 初期値の設定
ans = 0

for i in range(0, N - 1):
    # 二分探索の初期値を設定 ※ok,ng,midはindex番号を示す。
    ok = -1  # 0番目が答えになる可能性を踏まえて-1
    ng = len(A)
    cnt = 0
    while ng - ok > 1:  # 左側 - 右側
        mid = (ok + ng) // 2
        if is_ok(mid, i, K, A):
            ok = mid
        else:
            ng = mid
    ans += (ok + 1) - (i + 1)

print(ans)
