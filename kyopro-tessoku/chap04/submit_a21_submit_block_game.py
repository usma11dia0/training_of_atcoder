# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_u
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A21.py
# 参考　https://atcoder.jp/contests/tessoku-book/submissions/36580354

# 教訓
# for文の順番に注意
# r-l(右端-左端)の大きい順に計算
# r-lの値でfor文を逆から回す

# 配列内に-1や+1を入れてFor文を回す際は、out_of_rangeを常に意識する。

# for i in range(×, ×):
# 	P[i], A[i] = map(int, input().split())の時の、
# range(0,n)とrange(1,n+1)の違い
# range(0, n) = [1,2,3,4,0]
# range(1, n + 1) = [0,1,2,3,4]

# reversedとrangeの違い
# reversed(range(0,N-1)) = 0,1,2,3,4の逆
# range(n-1, 0 -1) = 5,4,3,2,1 という違いがある点に注意


# 考え方
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
for i in range(1, n + 1):
    p[i], a[i] = map(int, input().split())


dp = [[0] * (n + 1) for _ in range(0, n + 1)]

# for文の順番に注意
# r-l(右端-左端)の大きい順に計算
# → r-lの値でfor文を逆から回す
# LEN = r-l区間　例: n=6の時, LEN = 6-1= 5とn-1個になる
for LEN in range(n - 2, -1, -1):
    # reversed(range(0,N-1)) = 0,1,2,3,4の逆
    # range(n-1, 0 -1) = 5,4,3,2,1 という違いがある点に注意

    # 左端: 1からどこまで?
    # n = 6,LEN=3の時、LENが3となるのは(1,4)(2,5)(3,6)の3つ。
    # 3という値はn - LEN + 1で導出
    for l in range(1, n - LEN + 1):
        # 右端: 左端 + LEN
        r = l + LEN

        # 得点算出
        # 一番左のブロックを取り除く場合
        # 取り除いた後、(l,r)の範囲内にp[l-1]のブロックが残っている時に加点。それ以外は0点
        score_left = 0
        if l >= 2 and l <= p[l - 1] and p[l - 1] <= r:
            score_left = a[l - 1]

        # 一番右のブロックを取り除く場合
        # 取り除いた後、(l,r)の範囲内にp[r+1]のブロックが残っている時に加点。それ以外は0点
        score_right = 0
        if (
            r <= n - 1 and l <= p[r + 1] and p[r + 1] <= r
        ):  # r<=n-1の理由：例えばLEN=1, l=3の時、r=4となりp[r+1]はout_of_rangeとなるため、
            score_right = a[r + 1]

        # dp[l][r]の導出
        if l == 1:  # l=1となる時は、全て一番右のブロックを選択した場合のみ。
            dp[l][r] = dp[l][r + 1] + score_right
        elif r == n:  # r=nとなる時は、全て一番左のブロックを選択した場合のみ。
            dp[l][r] = dp[l - 1][r] + score_left
        else:
            dp[l][r] = max(dp[l - 1][r] + score_left, dp[l][r + 1] + score_right)

# 出力
Answer = 0
for i in range(1, n + 1):
    Answer = max(Answer, dp[i][i])
print(Answer)
