# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l
# answer

# 二分探索の関数を定義
# mid秒後に印刷されるチラシがK枚以上であればTrue,K枚未満であればFalse
def is_ok(mid: int, K: int, A: list) -> bool:
    # m秒後に印刷されるチラシの枚数を導出
    cnt = 0
    for a in A:
        cnt += mid // a
    if cnt >= K:
        return True
    else:
        return False


# 入力データの取得
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 初期値の設定
ng = 0  # 最小は0秒後にok
ok = 10**9  # 最大は何秒経ってもOKにならない → ∞秒後にOK

# 二分探索の実装
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(mid, K, A):
        ok = mid
    else:
        ng = mid

print(ok)
