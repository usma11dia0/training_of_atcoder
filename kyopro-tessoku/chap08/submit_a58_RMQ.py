# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bf
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A58.py

# 再起関数参考資料　C:\Users\usma1\OneDrive\ドキュメント\競プロノート\競技プログラミングの鉄則\a58

# 教訓： n以上で最小の値を求める → while xxx < n でループを抜けた時 (xxx=nでもループを抜ける)
#        変数前方のアスタリスクは、入力値分割。＊○○の値はリストとして格納される。

# セグメント木：「○○番目から△△番目までの要素の最大値を求めてください」といった区間に関するクエリを得意とするデータ構造

# セグメント木
class segtree:
    # 初期化
    def __init__(self, n):
        self.size = 1  # sizeはセグメント木の末端の最小単位
        while self.size < n:  # セグメント木の要素を2^kで示すため、size をn以上で最小の2^k数に設定
            self.size *= 2
        self.dat = [0] * (self.size * 2)  # セグメント木全体の要素数は、末端の要素数×2 - 1。最後の要素は無視。

    # クエリ1に対する処理
    def update(self, pos, x):  # posは末端の要素番号
        pos += self.size  # posは0-indexedなので、A[pos]のみに対応するセルの番号はpos + size
        self.dat[pos] = x
        while pos >= 2:  # 要素番号が末端の値から上端の1になるまで繰り返し。2も繰り返し対象。
            # セグメント木上で一つ上の階層の要素番号を取得
            pos //= 2  # a //= b  →  a = a // b に同じ
            # 一つ上の階層の値は、一つ下の階層(右下,左下)の中で最大のもの。
            self.dat[pos] = max(self.dat[pos * 2], self.dat[pos * 2 + 1])

    # クエリ2に対する処理
    # uは現在のセル番号, [a, b)はセルに対応する半開区間. [l, r)は求めたい半開区間

    # [l,r)に完全に含まれるセルを繋げて、その中で値が最大のものを返す事でクエリ2の処理が実行可能
    # → 再起関数により、セル(セグメント木の要素)を[l, r)に完全に含まれるまで分解していく
    def query(self, l, r, a, b, u):
        # [l, r)が[a, b)内に一切含まれない場合
        if r <= a or b <= l:
            return -1000000000  # －∞を返し再帰終了(目的が最大のため,該当しない場合は極小の値を入れる)
        # [l, r)が[a, b)内に完全に含まれる場合
        if l <= a and b <= r:
            return self.dat[u]  # 該当セルの要素を返し再帰終了
        # それ以外の場合([l, r)が[a, b)内に一部だけ含まれる場合)
        m = (a + b) // 2
        answerl = self.query(l, r, a, m, u * 2)  # 左下( [a, m) の区間 )のセルに対し再帰呼び出し
        answerr = self.query(l, r, m, b, u * 2 + 1)  # 右下( [m , b)の区間 )のセルに対し再帰呼び出し
        return max(answerl, answerr)


# 入力データの取得　(0-indexedで実装)
N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for i in range(Q)]

# クエリの処理
Z = segtree(N)
for q in queries:
    tp, *cont = q  # *cont内にqの0番目以外の要素がリストとして格納される。
    if tp == 1:
        pos, x = cont
        Z.update(pos - 1, x)  # pos は 1-indexed で入力されるので、update 関数の引数は pos - 1 にします
    if tp == 2:
        l, r = cont
        answer = Z.query(l - 1, r - 1, 0, Z.size, 1)  # 0-indexedでは最初に対応する半開区間は[0, size)
        print(answer)
