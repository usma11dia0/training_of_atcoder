# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m
# answer https://atcoder.jp/contests/tessoku-book/submissions/36461972
# 二分探索(bysect) https://atcoder.jp/contests/tessoku-book/submissions/36130862

# 教訓　配列の中のAが何番目の要素になるかを用いるかに二分探索が応用可能。
#      条件に該当しないケースの場合分けも忘れない。

# 解法(1) 二分探索法を用いる　(回答得られず)

# 関数定義
# 引数にインデックスをとり,配列aから対応する要素を取得してK以下かどうかを判定
def search(mid: int, k: int, a: list, a_i: int) -> bool:

    if a[mid] - a_i <= k:
        return True
    elif a[mid] - a_i > k:
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
    while left <= right:
        mid = (left + right) // 2
        if left == n - 1:
            r_i = left + 1
            break
        if left == right:
            r_i = left
            break
        if search(mid, k, a, a_i) == True:
            if a[mid] - a_i == k:
                r_i = mid + 1
                break
            left = mid + 1
        elif search(mid, k, a, a_i) == False:
            right = mid
    cnt += r_i - (i + 1)

print(cnt)
