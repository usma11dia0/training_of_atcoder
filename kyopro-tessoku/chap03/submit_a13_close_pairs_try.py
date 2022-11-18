# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m
# answer https://atcoder.jp/contests/tessoku-book/submissions/36461972
# 二分探索(bysect) https://atcoder.jp/contests/tessoku-book/submissions/36130862

# 教訓　求めたい条件を式で表してみる。
#       図式化して法則を見つける。

# 解法 二分探索法を用いる
# １．求めたい条件を式で表す。
# At - Ai <= K 移項すると
# At <= Ai + K 等号成立の条件は, At = Ai + K。不等式を満たすためのAtの最大値が求まる。
# AiもKも固定値のため、Atは一意に定まる。

# 3.2と同様の考え方で"答えはx以上か”を求める際に二分探索を用いると、
# "配列のある要素以降はAt以上である"が導出出来る。
# そのために、"配列の要素はAtの値以下であるか"を問として設定し、二分探索で求めるという方針。

# ２．Atが求まれば、求める値はAt - i - 1で導出される.


# 関数定義
# a[mid]がa_t以下であるかを判定
# YesであればTrue,NoであればFalseを返す。
def search(mid: int, a: list, a_t: int) -> bool:

    if a[mid] <= a_t:
        return True
    elif a[mid] > a_t:
        return False


# 入力データ取得
n, k = map(int, input().split())
a = list(map(int, input().split()))

# カウンター
cnt = 0

# 二分探索の実行 r_t(教科書の定義+1した値)の導出
for i, a_i in enumerate(a):
    # 配列aのインデックス(始めと終わり)を取得
    left = 0
    right = n - 1

    # Atの値を導出する
    a_t = a_i + k

    while left <= right:
        mid = (left + right) // 2
        if left == right:
            r_i = left
            break
        if search(mid, a, a_t) == True:  # a[mid]がa_t以下
            left = mid + 1
        elif search(mid, a, a_i) == False:  # a[mid]がa_tより大きい
            right = mid
    if left != 6:
        cnt += r_i - (i + 1)
    else:
        cnt += r_i - i


print(cnt)
