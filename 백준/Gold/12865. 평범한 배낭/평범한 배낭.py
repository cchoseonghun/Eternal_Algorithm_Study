import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
  w, v = map(int, input().split())

  for j in range(1, K + 1):
    if w > j:
      arr[i][j] = arr[i - 1][j]
    else:
      arr[i][j] = max(arr[i - 1][j], arr[i - 1][j - w] + v)

print(arr[N][K])