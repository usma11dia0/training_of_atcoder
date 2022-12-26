# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bp
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap09/answer_A68.py

# 教訓

# 参考HP：
# https://www.momoyama-usagi.com/entry/math-risan15

# 用語解説
# 深さ優先探索：「とにかく行けるとこまで行ってそれ以上進めなくなったら一歩戻ってそこから探索する」という探索方法。
# 幅優先探索とは「出発点に近い点から順に探索する」という探索方法。

# 最大フロー用の辺の構造体 ※残余グラフ作成のための値を格納
class maxflow_edge:
    def __init__(self, to, cap, rev):
        self.to = to  # A→Bとすると,Bを示す。
        self.cap = cap  # capacity：流せる残りの容量を示す
        self.rev = rev  # reverse: 逆辺の頂点を示す。
        # 1 → 2の場合、行先である頂点2の隣接リストG[2]の何番目に1が入っているかを返す。


# 深さ優先探索
# pos:positionの略。行き先を示す。F:増加道の容量　G:隣接リスト used:訪問済みフラグリスト
def dfs(pos, goal, F, G, used):
    if pos == goal:
        return F  # ゴールに到着：フローを流せる！
    # 探索する
    used[pos] = True  # used[各頂点]：深さ優先探索で訪問済みか否かを示すフラグのリスト。
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


#  頂点 s から頂点 t までの最大フローの総流量を返す（頂点数 N、辺のリスト edges）
def maxflow(N, s, t, edges):
    # 初期状態の残余グラフを構築
    # （ここは書籍とは少し異なる実装をしているため、8 行目は G[a] に追加された後なので len(G[a]) - 1 となっていることに注意）
    G = [list() for i in range(N + 1)]
    # G(隣接リスト)内に残余グラフに必要な値を入れていく
    for a, b, c in edges:  # lenの解釈：revは隣接している頂点の隣接しているノードの数
        G[a].append(maxflow_edge(b, c, len(G[b])))  # a → b の矢印
        G[b].append(maxflow_edge(a, 0, len(G[a]) - 1))  # b → a の矢印

        # ※maxflow_edgeの第三引数 lenの解釈
        # len(G[b])は逆辺の頂点であるbの隣接リスト内にaが何番目に来るかを示す。
        # aは直後にG[b]隣接リスト内へ追加されるため、最後の要素になるはず。→ 隣接リストの長さで要素番号を取得
        # bも同様に最後の要素になるはず。しかし直前にG[a]隣接リスト内へ追加されたため、要素番号はlen-1.

        # (a, b, c) = (1, 2, 5)の時のG
        # G: [[], [<__main__.maxflow_ed...093FFD210>], [<__main__.maxflow_ed...0948C0890>], [], [], [], []]
        # Gの中にはmaxflow_edgeクラスで生成されたインスタンスがそれぞれリストの中に格納される。
        # G[1]: [<__main__.maxflow_ed...093FFD210>]　※リスト内にインスタンスが格納されている点に注意
        # G[1][0]: <__main__.maxflow_ed...093FFD210>
        # ・G[1][0].to: 2  ・G[1][0].cap: 5　・G[1][0].rev: 0 ※1 → 2のフローを示す
        # ・G[2][0].to: 1  ・G[2][0].cap: 0  ・G[2][0].rev: 0 ※2 → 1のフローを示す

    INF = 10**10  # フローが流せなくなるごとにdfsで0が返る。F＝０になるまで繰り返すのでINFの初期値は無限大にしておく。
    # Fは深さ優先探索にてmin(F, e.cap)となり、どんどん小さい値へ更新されていく。→初期値は無限大にしておく。
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
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]
# print(edges)
# 出力結果: [[1, 2, 5], [1, 4, 4], [2, 3, 4], [2, 5, 7], [3, 6, 3], [4, 5, 3], [5, 6, 5]]

# 答えを求めて出力
answer = maxflow(N, 1, N, edges)
print(answer)
