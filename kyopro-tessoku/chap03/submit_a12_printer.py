# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l
# answer

# 教訓 ① 答えに対しても二分探索が利用できる
#      二分探索が利用出来る代表的な例:
# 　　「答えがx以上か?」「f(x)＝Nとなるようなxは?」※fは単調増加or単調減少
#      ② 二分探索では関数を定義してコードを書くと可読性が上がる


# check関数の定義 (mid秒後のチラシが印刷されるのはK枚以上かどうかを判定)
# mid: left,rightの秒数の中間, k:目標枚数, n:N台のプリンター, a:プリンターが1秒に印刷できる枚数
def check(mid: int, k: int, n: int, a: int) -> bool:
    sum = 0
    for i in range(0, n):
        sum += mid // a[i]
    if sum >= k:
        return True
    else:
        return False


# 入力データ取得
n, k = map(int, input().split())
a = list(map(int, input().split()))

# left,rightの値は秒数の最小/最大値を指定する。
left = 1
right = 10**9

while left <= right:
    if left == right:
        break
    mid = (left + right) // 2  # 小数点以下切り捨て
    if check(mid, k, n, a) == True:
        right = mid
    elif check(mid, k, n, a) == False:
        left = mid + 1

print(left)
