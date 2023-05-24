import sys
input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  arr = list(map(int, input().split()))
  arr.sort()

  M = 0
  for i in range(N - 2):
    L = abs(arr[i] - arr[i + 2])
    M = max(M, L)
  print(M)