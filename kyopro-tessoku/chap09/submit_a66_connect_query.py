# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bn
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap09/answer_A66.py

# 教訓 連結 → どの頂点も行き来可能である。

# Union-Find 木
class unionfind:
    # n 頂点の Union-Find 木を作成
    # （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
    def __init__(self, n):  # nには頂点の数Nが入る。
        self.n = n
        self.par = [-1] * (n + 1)  # 最初は親が無い　※parは親を示す。全ての頂点に親がいないことを示す-1を代入。
        self.size = [1] * (n + 1)  # 最初はグループの頂点数が 1

    # 頂点 x の根を返す関数
    def root(self, x):
        # 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
        while self.par[x] != -1:
            x = self.par[x]
        return x

    # 要素 u, v を統合する関数
    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            # u と v が異なるグループのときのみ処理を行う
            # Union By Sizeによる場合分け。頂点数の多いグループの根を上に持っていく
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    #  要素 u と v が同一のグループかどうかを返す関数
    def same(self, u, v):
        return self.root(u) == self.root(v)


# 入力
N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for i in range(Q)]

# クエリの処理
uf = unionfind(N)
for tp, u, v in queries:
    if tp == 1:
        uf.unite(u, v)
    if tp == 2:
        if uf.same(u, v):
            print("Yes")
        else:
            print("No")
