# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bq
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap09/answer_A69.py

# 教訓

# 最大フロー用の辺の構造体
class maxflow_edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev


# 深さ優先探索
def dfs(pos, goal, F, G, used):
    if pos == goal:
        return F  # ゴールに到着：フローを流せる！
    # 探索する
    used[pos] = True
    for e in G[pos]:
        # 容量が 1 以上でかつ、まだ訪問していない頂点にのみ行く
        if e.cap > 0 and not used[e.to]:
            flow = dfs(e.to, goal, min(F, e.cap), G, used)
            # フローを流せる場合、残余グラフの容量を flow だけ増減させる
            if flow >= 1:
                e.cap -= flow
                G[e.to][e.rev].cap += flow
                return flow
    # すべての辺を探索しても見つからなかった…
    return 0


# 頂点 s から頂点 t までの最大フローの総流量を返す（頂点数 N、辺のリスト edges）
def maxflow(N, s, t, edges):
    # 初期状態の残余グラフを構築
    # （ここは書籍とは少し異なる実装をしているため、8 行目は G[a] に追加された後なので len(G[a]) - 1 となっていることに注意）
    G = [list() for i in range(N + 1)]
    for a, b, c in edges:
        G[a].append(maxflow_edge(b, c, len(G[b])))
        G[b].append(maxflow_edge(a, 0, len(G[a]) - 1))
    INF = 10**10
    total_flow = 0
    while True:
        used = [False] * (N + 1)
        F = dfs(s, t, INF, G, used)
        if F > 0:
            total_flow += F
        else:
            break  # フローを流せなくなったら、操作終了
    return total_flow


# 入力
N = int(input())
C = [input() for i in range(N)]

# 最大フローを求めたいグラフを構築する（辺の要素は (辺の始点の番号, 辺の終点の番号, 辺の容量) のタプル）
edges = []
for i in range(N):
    for j in range(N):
        if C[i][j] == "#":
            edges.append((i + 1, N + j + 1, 1))  # 青色→赤色の辺
for i in range(N):
    edges.append((2 * N + 1, i + 1, 1))  # 「s → 青色」の辺 (第一引数が固定(s))
    edges.append((N + i + 1, 2 * N + 2, 1))  # 「赤色 → t」の辺 (第二引数が固定(t))

# edges = [(1, 6, 1), (2, 6, 1), (2, 8, 1), (3, 10, 1), (4, 10, 1), (5, 9, 1), (5, 10, 1), (11, 1, 1), (6, 12, 1), (11, 2, 1), (7, 12, 1), (11, 3, 1), (8, 12, 1), (11, 4, 1), ...]
# len(edges) = 17

# 答えを求めて出力
answer = maxflow(2 * N + 2, 2 * N + 1, 2 * N + 2, edges)
print(answer)
