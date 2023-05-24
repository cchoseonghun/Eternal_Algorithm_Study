import sys
input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  arr = list(map(int, input().split()))
  arr.sort(reverse=True)
  C = N // 2

  result = [0] * N
  result[C] = arr[0]

  for i in range(1, N):
    if i % 2 == 1:
      result[C - i // 2 - 1] = arr[i]
    else:
      result[C + i // 2] = arr[i]
  
  M= 0
  for i in range(N):
    L = abs(result[i] - result[(i + 1) % N])
    M = max(M, L)
  print(M)