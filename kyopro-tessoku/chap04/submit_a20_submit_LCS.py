# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_t
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap04/answer_A20.py

# 教訓 ビット探索 2べき乗を応用し、3べき乗のケースを考えるのが本問の特徴
#      DP問題へ帰着させた際,dpの選択肢が3つになる
#      LCSはLongest-Common-Subsequence problemの略

# 　　 indexの対象を間違えない(SやTに対応するインデックスを要確認)

# 入力データ取得
S = list(input())  # 列
T = list(input())  # 行

# 空の配列を準備
dp = [[0] * (len(S) + 1) for _ in range(0, len(T) + 1)]
diagonal = 0
for i in range(1, len(T) + 1):  # 縦に進む
    for j in range(1, len(S) + 1):  # 横に進む
        if S[j - 1] == T[i - 1]:
            # 斜めに進む (sのi番目とtのj番目が一致していた場合)
            diagonal = dp[i - 1][j - 1] + 1
            dp[i][j] = max(diagonal, dp[i - 1][j], dp[i][j - 1])
        # 斜めに進まない場合 (sのi番目とtのj番目が一致していない場合) max内のdiagonalを除く
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(T)][len(S)])
