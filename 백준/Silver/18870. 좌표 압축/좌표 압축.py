import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
unique = list(set(arr))
unique.sort()
result = {}
for i, x in enumerate(unique):
  result[x] = i
for x in arr:
  print(result[x], end=' ')