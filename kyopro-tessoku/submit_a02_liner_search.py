# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_a
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A02.py

# 数値の取得
n, x = map(int, input().split())
a = list(map(int, input().split()))

yes_flag = False

for a_num in a:
    if a_num == x:
        yes_flag = True
        break
    else:  # わざわざ書かなくても良い
        yes_flag = False

if yes_flag:
    print("Yes")
else:
    print("No")
