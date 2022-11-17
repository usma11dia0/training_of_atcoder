# bisect
import bisect

n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n - 1):
    key = arr[i] + k
    # 移項すると key - arr[i] = k
    # 差がkピッタリになるkeyの値
    cnt += bisect.bisect(arr, key) - (i + 1)

print(cnt)
