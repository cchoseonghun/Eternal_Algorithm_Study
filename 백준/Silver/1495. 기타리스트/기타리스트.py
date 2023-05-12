N, S, M = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][S] = True

for i in range(1, N + 1):
  for j in range(M + 1):
    if not dp[i - 1][j]:
      continue
    else:
      if j - arr[i - 1] >= 0:
        dp[i][j - arr[i - 1]] = True
      if j + arr[i - 1] <= M:
        dp[i][j + arr[i - 1]] = True

result = -1
for i in range(M, -1, -1):
  if dp[N][i]:
    result = i
    break
print(result)