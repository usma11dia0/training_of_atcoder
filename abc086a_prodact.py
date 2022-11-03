# 数値の取得
a, b = map(int, input().split())


def judge(a, b):
    if a * b % 2 == 0:
        s = "EVEN"
    else:
        s = "ODD"
    return s


print(judge(a, b))
