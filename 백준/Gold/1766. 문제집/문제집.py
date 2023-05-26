import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
# arr[node] -> node에 연결된 노드 정보
arr = [[] for _ in range(N+1)]
# indegree[node] -> node에 연결된 진입차수 개수
indegree = [0] * (N+1)

for _ in range(M):
  x, y = map(int, input().split())
  arr[x].append(y)
  indegree[y] += 1

heap = []
for i in range(1, N+1):
  if indegree[i] == 0:
    heapq.heappush(heap, i)

while heap:
  target = heapq.heappop(heap)
  print(target, end=' ')
  for i in arr[target]:
    indegree[i] -= 1
    if indegree[i] == 0:
      heapq.heappush(heap, i)