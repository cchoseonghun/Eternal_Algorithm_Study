N, S, M = map(int, input().split())
arr = list(map(int, input().split()))
DP = [[False] * (M + 1) for _ in range(N + 1)]
DP[0][S] = True

for i in range(1, N + 1):
  for j in range(M + 1):
    if DP[i - 1][j]:
      x = j - arr[i - 1]
      y = j + arr[i - 1]
      if 0 <= x <= M:
        DP[i][x] = True
      if 0 <= y <= M:
        DP[i][y] = True

result = -1
for i in range(M, -1, -1):
  if DP[-1][i]:
    result = i
    break
print(result)