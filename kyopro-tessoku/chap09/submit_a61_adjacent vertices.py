# question https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bi
# answer https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap09/answer_A61.py

# 教訓

# 入力
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

# print(edges)
# 出力結果：[[1, 2], [2, 3], [3, 4], [3, 5]]

# 隣接リストの作成 (0-indexed)
G = [list() for i in range(N + 1)]  # G[i] は頂点 i に隣接する頂点のリスト

# print(G)
# 出力結果：[[], [], [], [], [], []]

for a, b in edges:
    G[a].append(b)  # 頂点 a に隣接する頂点として b を追加
    G[b].append(a)  # 頂点 b に隣接する頂点として a を追加

# print(G)
# 出力結果：[[], [2], [1, 3], [2, 4, 5], [3], [3]]

# 出力
for i in range(1, N + 1):  # 0-indexedのため,範囲は1～N
    output = ""  # 空の文字列を定義
    output += str(i)  # 頂点の番号を追加
    output += ": {"  # ：と { を追加
    output += ", ".join(map(str, G[i]))  # [1,3] → '1, 3'へ変更
    output += "}"
    print(output)
