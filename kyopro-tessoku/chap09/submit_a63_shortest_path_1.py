# question https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_an
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap09/answer_A63.py

# 教訓

from collections import deque

# 入力データ取得
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(0, M)]

# 隣接リストの作成
G = [list() for _ in range(0, N + 1)]  # 0-indexedのため N + 1
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

# 幅優先探索の初期化 (初期化はdist[i] = -1で実施する)
dist = [-1] * (N + 1)  # 答えを格納するリスト
dist[1] = 0  # 頂点1→頂点1の距離は必ず0
Q = deque()  # Qの中に最短距離xの頂点が格納されていく
Q.append(1)  # 下記のループで最初にキューの先頭を削除するため、初期値(頂点1)をキュー内に入れておく

# 幅優先探索
while len(Q) >= 1:
    pos = Q.popleft()  # Qの先頭を削除し、posへ代入
    for nex in G[pos]:  # 頂点posの隣接ノードを一つ一つ調べる
        if dist[nex] == -1:  # 頂点nex(posの隣)の最短距離がまだ記録されていなければ
            dist[nex] == dist[pos] + 1  # posの最短距離+1をnexの最短距離として記録
            Q.append(nex)  # posの最短距離+1の頂点を新たにキュー内へ追加

# 頂点1から各頂点までの最短距離を出力
for i in range(1, N + 1):
    print(dist[i])
