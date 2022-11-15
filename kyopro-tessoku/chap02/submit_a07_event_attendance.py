# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g
# answer

# 数値の取得
d = int(input())
n = int(input())

participants_list = []
for i in range(0, n):
    tmp = list(map(int, input().split()))
    participants_list.append(tmp)

# 要素数8の空リストを作成
diff_list = [0] * d

for participant in participants_list:
    l = participant[0] - 1
    r = participant[1]  # r日目は参加しているため,r+1日目に-1をする。
    diff_list[l] += 1

    #r日目がd日間のdである場合は-1にする必要なし。
    if r != d:
        diff_list[r] -= 1

# 累積和を出力
accu = 0
for diff in diff_list:
    accu += diff
    print(accu)
