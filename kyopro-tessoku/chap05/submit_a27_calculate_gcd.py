# question https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_o
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap05/answer_A27.py

# 教訓：

# 入力データの取得
A, B = map(int, input().split())

while A != 0 and B != 0:
    if A <= B:
        B = B % A
    elif A > B:
        A = A % B

if A == 0:
    print(B)
else:
    print(A)
