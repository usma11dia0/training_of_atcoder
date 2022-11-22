# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_u
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A21.py
# 参考　https://atcoder.jp/contests/tessoku-book/submissions/36580354

# 教訓
# # for文の順番に注意
# r-l(右端-左端)の大きい順に計算
# r-lの値でfor文を逆から回す

# 区間DP 二次元配列の第一要素と第二要素を区間に見立てて対応する。
# dp[l][r]の条件 (最後にdp[l][r]になるための直前の条件を調べる)
# dp[l-1][r]の状態から左端を取り除く
# dp[l][r+1]の状態から右端を取り除く
# → 注意点は,取り除く際にPiが存在するか → 取り除いた後に[l][r]の区間内にPiが含まれていればOK

# 具体例 入力例1の場合
# ブロック1を取り除く dp[1][4] → dp[2][4]
# i = 1
# Pi = P1 = 4, Ai = A1 = 20
# ブロック1を取り除く際、ブロック4は含まれているため得点が入る。よって +20点

# ブロック4を取り除く dp[2][4] → dp[2][3]
# i = 4
# Pi = P4 = 1, Ai = A4 = 10
# ブロック4を取り除く際、ブロック1は既にないため得点が入らない。よって+0点
# 以下同様


# 入力データ取得
n = int(input())
p = [0] * (n + 1)  # index - 1 が添え字に対応
a = [0] * (n + 1)  # index - 1 が添え字に対応
for i in range(0, n):
    p[i], a[i] = map(int, input().split())


dp = [[0] * (n + 1) for _ in range(0, n + 1)]

# for文の順番に注意
# r-l(右端-左端)の大きい順に計算
# → r-lの値でfor文を逆から回す
# LEN = r-l区間
for LEN in range(n - 1, 0, -1):  # 例: n=6の時, LEN = 6-1= 5とn-1個になる
    # 左端: 1からどこまで?
    # n = 6,LEN=3の時、LENが3となるのは(1,4)(2,5)(3,6)の3つ。
    # 3という値はn - LEN + 1で導出
    for l in range(1, n - LEN + 1):
        # 右端: 左端 + LEN
        r = l + LEN

        # 得点の初期化
        score_left = 0
        score_right = 0

        # 一番左のブロックを取り除く場合
        # 取り除いた後、(l,r)の範囲内にp[l-1]のブロックが残っている時 = 加点
        if l <= p[l - 1] <= r:
            score_left = dp[l - 1][r] + a[l - 1]
        # 取り除いた後、(l,r)の範囲内にp[l-1]のブロックが残っていない時
        elif l > p[l - 1] and p[l - 1] > r:
            score_left = dp[l - 1][r]

        # 一番右のブロックを取り除く場合
        # 取り除いた後、(l,r)の範囲内にp[r+1]のブロックが残っている時 = 加点
        # LEN=1, l=3, r=4の時、a[r+1]はout_of_rangeとなるため、r<=n-1の制約を追加
        elif r <= n - 1 and l <= p[r + 1] <= r:
            score_right = dp[l][r + 1] + a[r + 1]
        # 取り除いた後、(l,r)の範囲内にp[r+1]のブロックが残っていない時
        elif l > p[l - 1] and p[l - 1] > r:
            score_left = dp[l][r + 1]

        # 得点導出
        dp[l][r] = max(score_left, score_right)

print(dp)
