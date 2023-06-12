import sys
input = sys.stdin.readline
import heapq

N = int(input())
arr = []
for _ in range(N):
  _, S, E = map(int, input().split())
  arr.append((S, E))
arr.sort(key=lambda x: x[0])

classes = []
heapq.heappush(classes, arr[0][1])

for i in range(1, N):
  S, E = arr[i]
  target = heapq.heappop(classes)
  if target <= S:
    heapq.heappush(classes, E)
  else:
    heapq.heappush(classes, E)
    heapq.heappush(classes, target)

print(len(classes))