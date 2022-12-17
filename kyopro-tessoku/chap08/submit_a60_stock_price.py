from collections import deque

# 教訓：配列の先頭削除や先頭追加は遅い。
# これのみを行いたい場合は、deque(スタックとキューを合わせたもの)を用いると高速化する

# 入力
N = int(input())
A = list(map(int, input().split()))

# スタックの変化の再現
# （スタックには (日付, 株価) のタプルを記録する）
answer = [None] * N
level2 = deque()
for i in range(N):
    if i >= 1:
        level2.append((i, A[i - 1]))
        # level2(stack)の一番上が常に起算日になるように実装している。
        while len(level2) >= 1:
            kabuka = level2[-1][1]  # 株価はタプルの 2 番目の要素
            if kabuka <= A[i]:
                level2.pop()
            else:  # kabuka > A[i]の時
                break
    if len(level2) >= 1:
        answer[i] = level2[-1][0]  # 日付はタプルの 1 番目の要素
    else:
        answer[i] = -1

# answer を空白区切りで出力
print(*answer)
