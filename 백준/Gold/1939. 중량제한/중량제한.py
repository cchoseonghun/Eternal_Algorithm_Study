import sys
input = sys.stdin.readline
from collections import deque

def BFS(mid):
  visited = [False] * (N + 1)
  queue = deque([start_node])
  visited[start_node]
  while queue:
    v = queue.popleft()
    for i, weight in graph[v]:
      if not visited[i] and mid <= weight:
        visited[i] = True
        queue.append(i)
  return visited[end_node]

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
start, end = 1000000000, 1
for _ in range(M):
  A, B, C = map(int, input().split())
  graph[A].append((B, C))
  graph[B].append((A, C))
  start = min(start, C)
  end = max(end, C)

start_node, end_node = map(int, input().split())

result = 0
while start <= end:
  mid = (start + end) // 2
  if BFS(mid):
    result = mid
    start = mid + 1
  else:
    end = mid - 1
print(result)