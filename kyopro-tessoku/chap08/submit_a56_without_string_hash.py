# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bd
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A56.py

# ハッシュ化を用いず配列のスライスを用いた場合(TLEで不正解)

# 教訓：
# 文字列の比較で実行時間制限を超える場合は、文字列をハッシュ化(数値変換)して比較する
# ハッシュ化にはB進数化が用いられ、桁数が多くなる場合はmodによる余りで代用する。
# 余りは重複が発生する可能性がある(ハッシュ衝突)が、modの値を大きくすることで対処可能な場合が多い。

# ハッシュ化の詳細については以下参照
# C:\Users\usma1\OneDrive\ドキュメント\競プロノート\競技プログラミングの鉄則\tessoku_a56_string_hash.jpg


# 入力データの取得
N, Q = map(int, input().split())
S = str(input())

a = [None] * (Q + 1)
b = [None] * (Q + 1)
c = [None] * (Q + 1)
d = [None] * (Q + 1)

for i in range(1, Q + 1):
    a[i], b[i], c[i], d[i] = map(int, input().split())

for i in range(1, Q + 1):
    if S[a[i] - 1 : b[i]] == S[c[i] - 1 : d[i]]:
        print("Yes")
    else:
        print("No")
