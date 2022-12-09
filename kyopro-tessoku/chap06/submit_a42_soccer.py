# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ap
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap06/answer_A42.py

# 教訓：2^nの全探索 → 値を何か固定しての全探索を検討する。(本問の場合、A,Bの下限値)

# 入力データ取得
N, K = map(int, input().split())

A = [0] * (N + 1)
B = [0] * (N + 1)

# 関数定義
def GetScore(a: int, b: int, A: list, B: list, K: int) -> int:
    cnt = 0
    for i in range(1, N + 1):
        if a <= A[i] and A[i] <= a + K and b <= B[i] and B[i] <= b + K:
            cnt += 1
    return cnt

    # 下記の繰り返しはNG A,Bは生徒の能力で連動しているため、A[i],B[i]で繰り返す。
    # for A_coordinate in A:
    #     if a + K >= A_coordinate and a <= A_coordinate:  # 下限の条件(a以下はダメ)を忘れない
    #         for B_coordinate in B :
    #             if b + K >= B_coordinate and b <= B_coordinate: # 下限の条件(b以下はダメ)を忘れない
    #                 cnt += 1
    # return cnt


for i in range(1, N + 1):
    A[i], B[i] = map(int, input().split())

# A,Bの下限値を固定し全探索
answer = 0
for a in range(1, 101):
    for b in range(1, 101):
        score = GetScore(a, b, A, B, K)
        answer = max(answer, score)

print(answer)
