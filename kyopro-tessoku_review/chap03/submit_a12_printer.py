# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l
# answer

# 教訓 ① 答えに対しても二分探索が利用できる
#      二分探索が利用出来る代表的な例:
# 　　「答えがx以上か?」「f(x)＝Nとなるようなxは?」※fは単調増加or単調減少
#      ② 二分探索では関数を定義してコードを書くと可読性が上がる

# 入力データの取得
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 方針：答えに対して二分探索を実施
# １．m秒後にチラシを何枚印刷出来るかを計算
# ２．１の計算結果とKを比較(二分探索)
# ３．同じであれば処理終了

# 二分探索を実施する関数
# mid秒後のチラシが印刷されるのはK枚以上かどうかを判定
# → Trueである → K枚はmid秒以下で既に達成されている → 求める答えはleft秒後かつmid秒以下
# → Falseである → K枚はmid秒より後で達成される → 求める答えはmid+1秒後かつright秒未満
def check(
    mid: int,
    K: int,
    A: list,
) -> bool:
    # mid秒後に印刷されるチラシの枚数を求める
    sum = 0
    for a in A:
        sum += mid // a
    # mid秒後のチラシが印刷される枚数がK枚以上
    if sum >= K:
        return True
    else:
        return False


# 初期値の設定
left = 1
right = 10**9

while left <= right:
    if left == right:
        print(left)
        break
    mid = (left + right) // 2
    # 二分探索の実施
    result = check(mid, K, A)
    # 二分探索の結果がK以上
    if result == True:
        right = mid
    # 二分探索の結果がK未満
    elif result == False:
        left = mid + 1
