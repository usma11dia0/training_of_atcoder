# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bh
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A60.py

# 教訓：stackを使わないこの解答はTLE
#      ※forの二重ループで,O(N^2)。N = (2*10^5)^2で10^9を超えてしまうため。
#      ※配列の先頭追加、先頭削除は実行速度が遅い。先頭追加や先頭削除はdequeが優れている

# 入力データの取得
N = int(input())
A = list(map(int, input().split()))  # 0-indexed

# 株価データを格納
date_and_price = []
# for i, a in enumerate(A):
#     date_and_price.append([i + 1, a])

for i in range(0, N):
    if i == 0:
        print("-1")
        date_and_price.append([i + 1, A[i]])
    # date_and_price内を逆順で調べていく。
    else:
        for j in range(len(date_and_price) - 1, -1, -1):
            if A[i] < date_and_price[j][1]:
                print(date_and_price[j][0])  # date_and_priceの要素番号を出力
                date_and_price.append([i + 1, A[i]])
                break
            elif A[i] >= date_and_price[j][1]:
                date_and_price.remove(date_and_price[j])  # date_and_priceの該当要素を削除
                if not date_and_price:
                    print("-1")
                    date_and_price.append([i + 1, A[i]])
