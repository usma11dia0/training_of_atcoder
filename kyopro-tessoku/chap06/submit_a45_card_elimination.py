# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_as
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap06/answer_A45.py

# 教訓：不変量に注目するためには、まず試しに具体例を考えてみて法則を見つける。
#       その際、スコア化という手段により法則性(今回の場合不変量)が可視化されることがある。

# 入力データ取得
N, C = input().split()
N = int(N)

A_str = str(input())
A = []
for str in A_str:
    A.append(str)

score = 0
for a in A:
    if a == "W":
        score += 0
    elif a == "B":
        score += 1
    elif a == "R":
        score += 2

result = None
if score % 3 == 0:
    result = "W"
elif score % 3 == 1:
    result = "B"
elif score % 3 == 2:
    result = "R"

if result == C:
    print("Yes")
else:
    print("No")