# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap02/answer_A07.py

# 教訓：出席者の前日比
# インデックス指定する際は、リストの範囲に要注意。

# 入力データの取得
D = int(input())
N = int(input())
L = [None] * (N + 1)
R = [None] * (N + 1)

for i in range(1, N + 1):
    L[i], R[i] = map(int, input().split())

# 出席者の前日比リストを作成
B = [0] * (D + 2)  # 0-indexedのため+1。さらに最終日対策のため +1
for i in range(1, N + 1):
    B[L[i]] += 1
    B[R[i] + 1] -= 1  # R[i]日目はまだ出席している点に注意

# 前日比リストの累積和を出力
ans = 0
for i in range(1, D + 1):
    ans += B[i]
    print(ans)
