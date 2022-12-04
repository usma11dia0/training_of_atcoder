# question https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_bn
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap06/answer_A39.py

# 教訓：貪欲法は、「１ステップ先だけを考えたときの最善手を選び続ける」というもの
# 　　　区間スケジューリングでは終了時間が短いものを選択していく事がベスト ※最初に小さい順にソートしておく必要がある。
#       終了時刻でソートするためには、各時刻を配列で一緒に格納する必要がある。※配列の0番目の要素順にソートされる点に要注意

# 入力データ取得
N = int(input())

A = []
for i in range(0, N):
    L, R = map(int, input().split())
    A.append([R, L])  # 終了時刻を要素0番目に持ってくる。

A.sort()

# 貪欲法により答えを導出
cnt = 0
CurrentTime = 0
for i in range(0, N):
    if A[i][1] >= CurrentTime:
        CurrentTime = A[i][0]
        cnt += 1

print(cnt)
