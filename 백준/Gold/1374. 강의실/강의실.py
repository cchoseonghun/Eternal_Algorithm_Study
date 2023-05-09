import sys
input = sys.stdin.readline
import heapq

N = int(input())
arr = []
for _ in range(N):
  _, start, end = map(int, input().split())
  heapq.heappush(arr, (start, end))

heap = []  # 배정된 강의실
end = heapq.heappop(arr)[1]
heapq.heappush(heap, end)
answer = 1

for i in range(N-1):
  new_start, new_end = heapq.heappop(arr)
  end = heapq.heappop(heap)

  if new_start < end:
    heapq.heappush(heap, end)
    heapq.heappush(heap, new_end)
    answer += 1
  else:
    heapq.heappush(heap, new_end)

print(answer)