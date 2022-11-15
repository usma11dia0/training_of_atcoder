# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_c
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A02.py

# 数値の取得
n, k = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

yes_flag = False

for p_num in p:
    for q_num in q:
        sum = 0
        sum = p_num + q_num
        if sum == k:
            yes_flag = True
            break

if yes_flag:
    print("Yes")
else:
    print("No")
