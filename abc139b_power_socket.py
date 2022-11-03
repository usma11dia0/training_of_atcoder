# 学び a=0の時など、イレギュラーケースの対応についても留意する。

# 方針
# 4 , 10
# 1個　4口
# 2個　3口 + 4口
# 3個　3口 + 3口 + 4口
# answer 3

# 8, 9
# 1個　8口
# 2個　7口 + 8口
# answer 2

# # テスト用
a = 20
b = 1

# 数値の取得
# a, b = map(int, input().split())

sum = 0
counter = 0

while sum < b:
    if b == 1:
        counter = 0
        break
    elif sum == 0:
        sum = a
    else:
        sum -= 1
        sum = sum + a

    counter += 1

print(counter)
