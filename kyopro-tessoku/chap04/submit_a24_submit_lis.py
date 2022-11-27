# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_x
# answer

# 教訓 lis_simple 17行目以降のfor文ループに対して対応を考える。
#      A_jを1から順に調べずに済む方法はないか？

#      二分探索を用いる事は出来ないか？
#      L[x]：長さxの部分裂の最後の要素として考えられる最小値の配列
#      L[pos] < A_iを満たすposの最大値を求める。→ posに1を加算した値が答え
#      f(x) < Nを満たすxの最大値は？の言い換え

#      二分探索が利用出来る代表的な例:
# 　　「答えがx以上か?」「f(x)＝Nとなるようなxは?」※fは単調増加or単調減少
#      ② 二分探索では関数を定義してコードを書くと可読性が上がる

import bisect

# 入力データ取得 (Aは0番目から始まることに注意)
N = int(input())
A = list(map(int, input().split()))

LEN = 0  # 配列Lの長さ
L = []
dp = [None] * (N)  # 0番目から始まっているため、実際の値は+1した値

for i in range(0, N):
    # 配列L内でA[i]が挿入できる位置 →　L[pos] < A_iを満たすposの最大値
    pos = bisect.bisect_left(L, A[i])  # ソートされた順序を保ったまま A[i] を L に挿入できる点を探し当てる。
    
    # dp[i]:最後の要素がA_iである部分列のうち、最長のものの長さ
    # 各値を+1すると、鉄則本のdpの値になる。
    dp[i] = pos

    # 配列Lを更新
    # 二分探索の結果、最終尾が指定された場合。Lにその値を追加
    if dp[i] >= LEN:
        L.append(A[i])
        LEN += 1
    # 二分探索の結果、最終尾以外が指定された場合。A_iがL内に挿入される位置の値をA_iへ更新する
    else:
        L[dp[i]] = A[i]

# 答えを出力
print(LEN)
