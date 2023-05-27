import sys
input = sys.stdin.readline
import heapq

N = int(input())
arr = []
for _ in range(N):
  d, c = map(int, input().split())
  arr.append((d, c))
arr.sort()

heap = []
for d, c in arr:
  heapq.heappush(heap, c)
  while len(heap) > d:
    heapq.heappop(heap)

print(sum(heap))