# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bl
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap09/answer_A64.py

# 教訓 ダイクストラ法に関する分かりやすいYoutube動画　https://www.youtube.com/watch?v=e6X2gDTZYCQ
#      ※離散数学入門#5: 最短経路問題：ダイクストラ法とワーシャル–フロイド法

import heapq  # 未確定頂点の中で最小の値を導出するために優先度付きキューを利用

# 入力
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

# 隣接リストの作成（重み付きグラフなので、各辺について (隣接頂点, 重み) のタプルを記録する）
G = [list() for i in range(N + 1)]
for a, b, c in edges:
    G[a].append((b, c))
    G[b].append((a, c))

# 配列・キューの初期化（キューには (距離, 頂点番号) のタプルを記録する）
INF = 10**10
kakutei = [False] * (N + 1)  # 未確定頂点かどうかを判定するフラグ
cur = [INF] * (N + 1)  # curは頂点1からの最短距離の暫定値
cur[1] = 0  # 頂点1～頂点1の最短距離は0
Q = []  # 未確定頂点とその暫定距離がタプルで格納された優先度付きキュー (暫定距離, 頂点番号)
heapq.heappush(Q, (cur[1], 1))  # 優先度付きキューQに距離0, 頂点番号1の要素を追加する

# ダイクストラ法
while len(Q) >= 1:
    # 未確定頂点の中で最小のものを抽出する。(この時頂点1→頂点xの最短距離が確定)
    # （ここでは、優先度付きキュー Q の最小要素を取り除き、その要素の 2 番目の値（頂点番号）を pos に代入する）
    pos = heapq.heappop(Q)[1]
    # 最初のループの挙動
    # １．Q = [(0, 1)]の先頭要素を取り除く。Q=[]になる
    # ２. pos = (0, 1)が代入されるため、その要素の2番目の値(1:頂点番号)を[1]で取り出す

    # Q の最小要素が「既に確定した頂点」の場合
    if kakutei[pos] == True:
        continue  # 既に確定した場合は次のwhileループへ進む

    # 未確定頂点の中でかつ最小の頂点を確定させる
    kakutei[pos] = True

    # 確定した頂点の隣接ノード(未確定頂点)の暫定値を更新する。
    for e in G[pos]:  # 確定した頂点の隣接ノードのe(距離、頂点番号)を全て求める。
        if cur[e[0]] > cur[pos] + e[1]:  # 隣接ノードの現在の値より、確定ノード+隣接ノードの値が小さい場合
            cur[e[0]] = cur[pos] + e[1]  # 隣接ノードの値を確定ノード+隣接ノードの値に更新
            heapq.heappush(Q, (cur[e[0]], e[0]))  # 優先順位付きキューに新たに更新した要素を追加

    # pos = 1の時の各変数の値 (頂点1を確定させた場合)
    # print(G)
    # [[],[(2, 15),(4, 20)],[(1, 15), (3, 65), (5, 4)]…]
    # G[1] = [(2, 15),(4, 20)] #頂点1の全隣接ノード
    # e = (2, 15) or (4, 20) #頂点1の各隣接ノード

    # print(cur)
    # [10**10, 0, 10**10, 10**10, 10**10…]

# 答えを出力
for i in range(1, N + 1):
    if cur[i] != INF:
        print(cur[i])
    else:
        print("-1")
