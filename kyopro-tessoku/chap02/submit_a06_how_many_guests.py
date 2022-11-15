# question https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap02/answer_A06.py

# 数値の取得
n, q = map(int, input().split())
a = list(map(int, input().split()))

question_list = []
for i in range(0, q):
    tmp = list(map(int, input().split()))
    question_list.append(tmp)

# 全体の累積和を計算
accu = 0
accu_list = []
for a_num in a:
    accu += a_num
    accu_list.append(accu)

for question in question_list:
    l = question[0] - 1
    r = question[1] - 1
    # 1日目が開始の場合はn-1日目までの累計を引く
    if l != 0:
        ans = accu_list[r] - accu_list[l - 1]
        print(ans)
    # 1日目が開始の場合は引く必要なし
    else:
        ans = accu_list[r]
        print(ans)
