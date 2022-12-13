# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bd
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A56.py

# ハッシュ化を用いず配列のスライスを用いた場合(TLEで不正解)

# 教訓：
# map関数の挙動；第二引数のイテラブルな要素全てに対し、第一引数の関数を適用させる。
# ord()は文字をUnicordに変換する関数→小文字のaが97
# a～zにそれぞれ1,2,3…と番号を付けたいなら、ord(x) - ord(a) + 1を指定すればよい。


# 文字列の比較で実行時間制限を超える場合は、文字列をハッシュ化(数値変換)して比較する
# ハッシュ化にはB進数化が用いられ、桁数が多くなる場合はmodによる余りで代用する。
# 余りは重複が発生する可能性がある(ハッシュ衝突)が、modの値を大きくすることで対処可能な場合が多い。

# ハッシュ化の詳細については以下参照
# C:\Users\usma1\OneDrive\ドキュメント\競プロノート\競技プログラミングの鉄則\tessoku_a56_string_hash.jpg

# 漸化式のような形(i+1 = i + xxx)の場合、必ず初期値を設定する。


# 入力データの取得
N, Q = map(int, input().split())
S = str(input())
queries = [list(map(int, input().split())) for _ in range(0, Q)]

# 文字を数値に変換
T = list(map(lambda s: ord(s) - ord("a") + 1, S))
# 先頭に0を追加
T.insert(0, 0)

# B進数のB(100のn乗 % MOD)を前計算
MOD = 2147483647
power100 = [None] * (N + 1)

# 漸化式で表すため初期値を設定する
power100[0] = 1
for i in range(0, N):
    power100[i + 1] = power100[i] * 100 % MOD  # 漸化式のため繰り返しはN-1でOK。

# H[1], H[2]……H[N](ハッシュ値)を計算
H = [None] * (N + 1)
H[1] = T[1] * power100[0]
for i in range(1, N):
    H[i + 1] = (H[i] * 100 + T[i + 1]) % MOD

# ハッシュ値を求める関数
def hash_value(l, r):
    if l == 1:
        return H[r]
    else:
        return (H[r] - H[l - 1] * power100[r - l + 1]) % MOD


# クエリに答える
for a, b, c, d in queries:
    hash1 = hash_value(a, b)
    hash2 = hash_value(c, d)
    if hash1 == hash2:
        print("Yes")
    else:
        print("No")
