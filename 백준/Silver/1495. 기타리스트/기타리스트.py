N, S, M = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][S] = True

for i in range(1, N + 1):
  for j in range(M + 1):
    if dp[i - 1][j]:
      a = j - arr[i - 1]
      b = j + arr[i - 1]
      if 0 <= a <= M:
        dp[i][a] = True
      if 0 <= b <= M:
        dp[i][b] = True

result = -1
for i in range(M, -1, -1):
  if dp[-1][i]:
    result = i
    break
print(result)