# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_o
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap03/answer_A15.py

# 教訓：重複削除にはset型(集合型)を用いる。
#      set型には順序関係がないため、ソートする際はリストにする。
#      pythonにはsize()はない。配列の要素数を取得する場合はlen()を用いる。
#      めぐる式二分探索の際、ok,ngの範囲に注意する。

# 二分探索用の関数を定義
# X[mid]の値がaよりも小さい場合,True。そうでない場合Falseを返す。
# X[mid]の値がaと等しい場合、-1を返す。
def is_small(mid: int, a: int, X: list) -> bool:
    if X[mid] < a:
        return True
    elif X[mid] > a:
        return False
    elif X[mid] == a:
        return -1


# 入力データの取得
N = int(input())
A = list(map(int, input().split()))

# 配列Aを小さい順に並び変え,重複を削除した配列Xを生成
# 配列Xを一旦Set型へ変換して重複を削除、その後再度リスト化
X = list(set(A))
X.sort()

# Aの要素がX内の何番目に位置するかを二分探索により導出
for a in A:
    ok = -1
    ng = len(X)
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_small(mid, a, X) == True:
            ok = mid
        elif is_small(mid, a, X) == False:
            ng = mid
        elif is_small(mid, a, X) == -1:
            print(mid + 1, end=" ")
            break
