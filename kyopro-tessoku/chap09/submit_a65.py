# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bm
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap09/answer_A65.py

# 教訓　printの使い方
# リストの出力

# print(*[1, 2, 3])
# 1 2 3

# print(*[1, 2, 3], sep='-')
# 1-2-3

# ※注意 リストにそのままsepを用いても、リスト自体が区切りになるため意味がない。
# print([1, 2, 3], sep='-')
# [1, 2, 3]

# 入力データの取得
N = int(input())
A = [0] * 2 + list(map(int, input().split()))  # A_iは要素番号2から始まり、0-indexedであるため[0]*2を追加。
# print(A)
# 出力：[0, 0, 1, 1, 3, 2, 4, 4]　要素番号2からAの値が格納されている

# 隣接リストの作成
G = [list() for _ in range(0, N + 1)]  # 0-indexedのためN+1
for i in range(2, N + 1):
    G[A[i]].append(i)  # 上司 → 部下の方向に辺を追加
    # A[i]に社員iの上司が記載されている。

# print(G)  # G:社員iにどのような部下がいるかを示す。
# 出力： [[], [2, 3], [5], [4], [6, 7], [], [], []]
#      要素番号が上司。要素が部下。

# 動的計画法 (dp[x]は社員xの部下の数)
dp = [0] * (N + 1)
for i in range(N, 0, -1):  # 要素番号が末端のものから調べていく。
    for j in G[i]:  # 社員iの部下を一人ひとり抽出 ※G[i]に何も入っていなければ次へ進む
        dp[i] += dp[j] + 1  # dp[i]は社員iの部下, +1で社員i自身を示す。

# 答え (dp[1], dp[2], ..., dp[N]) を空白区切りで出力
print(*dp[1:])
