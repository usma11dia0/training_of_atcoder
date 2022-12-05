# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_an
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap06/answer_A40.py

# 教訓：配列の要素番号をA_iメートルとみなして各棒の個数をカウントする。
#       N本の棒を基準に配列を作成すると、2*10**5通りになってしまうため、
#       A_iメートルの長さで配列を作成する。(100通り)

# 入力データ取得
N = int(input())
A = list(map(int, input().split()))

cnt = [0] * (100 + 1)  # 0番目の要素を加味して +1。cnt[100]は101番目


for i in range(0, N):
    cnt[A[i]] += 1


# 答えを導出する
ans = 0
for i in range(1, 101):
    ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6

print(ans)
