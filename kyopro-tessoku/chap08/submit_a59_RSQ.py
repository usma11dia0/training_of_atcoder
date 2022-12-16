# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bg
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A59.py

# 再起関数参考資料　C:\Users\usma1\OneDrive\ドキュメント\競プロノート\競技プログラミングの鉄則\a58

# 教訓：0-indexed → 3番目を指定する際は-1した2を指定する必要がある

# セグメント木(0-indexed)
class segtree:
    # 初期化
    def __init__(self, n):
        # セグメント木の各階層に0を入れる。
        # 与えられたn <= 末端の要素数2^kを満たす最小の2^k(self.size)を求める
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.dat = [0] * (self.size * 2)  # セグメント木全体の要素数は末端の要素数×2-1 (先頭の要素無視のため-1はしない)

    # dat[pos]の値をxに更新。セグメント木も同時に更新する。
    def update(self, pos, x):  # 0-indexedのためposの引数は-1された状態で渡す
        # セグメント木の末端要素の値を更新
        pos = pos + self.size
        self.dat[pos] = x
        # 末端から上階層の要素も更新する
        while pos >= 2:
            pos //= 2
            # 上階層の値は(左下,右下)の合計値
            self.dat[pos] = self.dat[pos * 2] + self.dat[pos * 2 + 1]

    # 求めたい合計値の区間[l,r)がu番目セルの区間[a,b)に完全に含まれるまで再帰を繰り返す関数
    def query(self, l, r, a, b, u):
        # 合計値の区間[l,r)がu番目セルの区間[a,b)に全く含まれない場合
        if r <= a or b <= l:  # 各区間の=に要注意。
            return 0
        # 合計値の区間[l, r)がu番目セルの区間[a,b)に全て含まれる場合
        if l <= a and b <= r:
            return self.dat[u]
        # 合計値の区間[l,r)がu番目セルの区間[a,b)に一部だけ含まれている場合
        m = (a + b) // 2
        # 左下セルに対してquery関数を再帰呼び出し
        answerl = self.query(l, r, a, m, u * 2)
        answerr = self.query(l, r, m, b, u * 2 + 1)
        return answerl + answerr


# 入力データの取得
N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(0, Q)]

Z = segtree(N)

# クエリの処理
for q in queries:
    tq, *cont = q
    if tq == 1:
        pos, x = cont
        Z.update(pos - 1, x)
    if tq == 2:
        l, r = cont
        answer = Z.query(l - 1, r - 1, 0, Z.size, 1)
        print(answer)
