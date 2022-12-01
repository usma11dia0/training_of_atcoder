# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ae
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap05/answer_A31.py

# 教訓：


# 入力データの取得
N = int(input())
A_1 = N // 3  # 3の倍数で割り切れる数の個数
A_2 = N // 5  # 5の倍数で割り切れる数の個数
A_3 = N // 15  # 15の倍数で割り切れる数の個数
print(A_1 + A_2 - A_3)
