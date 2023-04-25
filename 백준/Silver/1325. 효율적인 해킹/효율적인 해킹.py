import sys
sys.setrecursionlimit(100000)
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  x, y = map(int, input().split())
  graph[y].append(x)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

max_count = 0
result = []
for i in range(1, N+1):
  visited = [False] * (N+1)
  bfs(graph, i, visited)
  counting = visited.count(True)
  if max_count < counting:
    max_count = counting
    result = [i]
  elif max_count == counting:
    result.append(i)

for x in result:
  print(x, end=' ')