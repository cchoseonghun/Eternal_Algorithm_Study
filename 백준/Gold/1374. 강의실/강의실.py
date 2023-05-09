import sys
input = sys.stdin.readline
import heapq

N = int(input())
arr = []
for _ in range(N):
  _, start, end = map(int, input().split())
  heapq.heappush(arr, (start, end))

heap = []
end = heapq.heappop(arr)[1]
heapq.heappush(heap, end)

while arr:
  new_start, new_end = heapq.heappop(arr)
  end = heapq.heappop(heap)

  if new_start < end:
    heapq.heappush(heap, end)
    heapq.heappush(heap, new_end)
  else:
    heapq.heappush(heap, new_end)

print(len(heap))