import sys
input = sys.stdin.readline
import heapq

N = int(input())
arr = []
for i in range(N):
  d, c = map(int, input().split())
  arr.append((d, c))
arr.sort()

result = []
for d, c in arr:
  heapq.heappush(result, c)
  if d < len(result):
    heapq.heappop(result)
print(sum(result))