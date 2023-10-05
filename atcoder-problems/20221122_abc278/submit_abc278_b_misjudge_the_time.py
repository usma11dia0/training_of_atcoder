# question https://atcoder.jp/contests/abc278/tasks/abc278_b

import sys

# 入力データ
H, M = map(int, input().split())

for h in range(0, 24):
    for m in range(0, 60):

        # str変換
        H = str(H)
        M = str(M)

        # 2桁の0埋め
        H = H.zfill(2)
        M = M.zfill(2)

        # A, B, C, D取得(str型)
        A, B = H[0], H[1]
        C, D = M[0], M[1]

        # 桁入れ替えのH, M
        AC = A + C  # 桁入れ替え後のH
        BD = B + D  # 桁入れ替え後のM

        # int型変換
        H = int(H)
        M = int(M)
        AC = int(AC)
        BD = int(BD)

        # 桁入れ替え後の値を判定
        if 0 <= AC and AC < 24 and 0 <= BD and BD < 60:
            print(H, end=" ")
            print(M, end=" ")
            sys.exit(0)

        # 分刻みで+1
        M += 1
        if M > 59:  # Mが60を上回った場合,Hのループへ移る
            M = 0
            break

    # 時間刻みで+1
    H += 1
    if H > 23:
        H = 0
