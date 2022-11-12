# question https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b
# 解説動画(分前後)

# 数値の取得
n, a, b = map(int, input().split())
s = str(input())

# 合格者人数
num_pass = 0

# B内の順位
rank_b = 1

for char in s:
    if char == "a":
        if a + b > num_pass:
            num_pass += 1
            print("Yes")
        else:
            print("No")
    elif char == "b":
        if a + b > num_pass and b >= rank_b:
            num_pass += 1
            rank_b += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
