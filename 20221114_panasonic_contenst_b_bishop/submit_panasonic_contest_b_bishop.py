# question https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_b
# answer（15:00以降) https://www.youtube.com/watch?v=bHzohtVsG0Q

import math

# 数値の取得
h, w = map(int, input().split())

all = h * w
if h == 1 or w == 1:
    print(1)
else:
    # elif (h % 2 == 0 and w % 2 != 0) or (h % 2 != 0 and w % 2 == 0):
    ans = math.ceil(all / 2)
    print(ans)
