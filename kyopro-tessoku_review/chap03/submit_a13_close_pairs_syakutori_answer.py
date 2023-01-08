# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m
# answer

# 教訓：しゃくとり法の考え方の基礎は、自明な範囲の探索を再度実行しないこと

# 参考資料：https://www.akiradeveloper.com/post/syakutori/

# 入力データ取得
n, k = map(int, input().split())
a = list(map(int, input().split()))

# 配列の準備　#要素番号iのもとで、問題文の条件を満たす最大のAの要素番号の配列
# ※番号r[i]は条件を満たす要素番号+1になる。
r = [None] * n

# しゃくとり法の実施
# n番目は該当なしのため。
for i in range(0, n - 1):

    # スタート位置の指定
    if i == 0:
        r[i] = 0
    else:  # iが0以外の場合
        r[i] = r[i - 1]  # 更新されたiのr[i]の値を求める際は、i-1で確定したrの値からスタートする。

    # r[i]の値が配列Aの要素番号を超えない,かつ要素番号r[i]のもとでさえ条件を満たす場合
    while r[i] < n - 1 and a[r[i] + 1] - a[i] <= k:
        # 要素番号r[i]の値を1増やす(上記で条件を満たしており、r[i]が最大ではないため)
        r[i] += 1
    # whileループを抜けた場合、要素番号r[i]はiの下で条件を満たす最大の要素番号+1となっている。(0-indexedであるため)

# 結果の出力
ans = 0
for i in range(0, n - 1):
    ans += r[i] - i

print(ans)


# # 入力
# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# # 配列の準備
# r = [None] * n

# # しゃくとり法
# for i in range(0, n - 1):
#     # スタート地点を決める
#     if i == 0:
#         r[i] = 0
#     else:
#         r[i] = r[i - 1]

#     # ギリギリまで増やしていく
#     while r[i] < n - 1 and a[r[i] + 1] - a[i] <= k:
#         r[i] += 1

# # 出力
# Answer = 0
# for i in range(0, n - 1):
#     Answer += r[i] - i
# print(Answer)
