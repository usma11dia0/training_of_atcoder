# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_u
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A21.py
#
# 教訓

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
