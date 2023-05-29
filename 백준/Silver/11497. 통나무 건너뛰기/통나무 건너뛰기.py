import sys
input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  arr = list(map(int, input().split()))
  arr.sort()

  m = 0
  for i in range(N - 2):
    m = max(m, arr[i + 2] - arr[i])
  print(m)