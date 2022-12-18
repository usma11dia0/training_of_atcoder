# question https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_am
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap09/answer_A62.py

# 教訓

# 入力
import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

# 深さ優先探索を行う関数（pos は現在位置、Gは隣接リスト, visited[x] は頂点 x が青色かどうかを表す真偽値 ）
def dfs(pos, G, visited):  # pos:int, G:list, visited:list
    visited[pos] = True  # 現在位置を青色に塗る(訪問済みにする)
    for i in G[pos]:  # 現在位置の隣接ノード(i)を一つ一つ調べる。後半で再帰呼び出しているため、隣接リストを網羅出来る。
        if visited[i] == False:  # もし隣接ノードが白色(未訪問)だったら、
            dfs(i, G, visited)  # 隣接ノードiを現在位置としてdfsを再帰呼び出し
    # 再帰毎にdfs()のforループの残り(callstack)が溜まっていく
    # for i in G[pos]:のループが終わり次第、dfs()の返り値でNoneが返る
    # Noneが返った後は溜まったcallbackを処理する。 →　本の一つ戻るを表現


# 入力
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

# 隣接リストの作成
G = [list() for i in range(N + 1)]  # G[i] は頂点 i に隣接する頂点のリスト
for a, b in edges:
    G[a].append(b)  # 頂点 a に隣接する頂点として b を追加
    G[b].append(a)  # 頂点 b に隣接する頂点として a を追加

# print(G)
# 出力結果：[[], [2, 3], [1, 4], [1, 4], [2, 3, 5, 6], [4], [4]]

# 深さ優先探索
visited = [False] * (N + 1)
dfs(1, G, visited)

# print(visited)　※visited[x] は頂点 x が青色かどうかを表す真偽値
# 出力結果：[False, True, True, True, True, True, True]

# 連結かどうかの判定（answer = True のとき連結）
answer = True
for i in range(1, N + 1):
    if visited[i] == False:
        answer = False

# 答えの出力
if answer == True:
    print("The graph is connected.")
else:
    print("The graph is not connected.")


# 鉄則本の入力例
# 6 6
# 1 2
# 1 3
# 2 4
# 3 4
# 4 5
# 4 6
