import sys
input = sys.stdin.readline
for _ in range(int(input())):
  N = int(input())
  dp = [0] * 101
  dp[1] = 1
  dp[2] = 1
  dp[3] = 1
  for i in range(4, 101):
    dp[i] = dp[i-3]+dp[i-2]
  print(dp[N])