import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []

for _ in range(N):
  x, y = map(int, input().split())
  heapq.heappush(heap, (x, y))

start, end = heapq.heappop(heap)
result = 0
while heap:
  x, y = heapq.heappop(heap)
  if x <= end:
    end = max(end, y)
  else:
    result += end - start
    start = x
    end = y
result += end - start
print(result)
