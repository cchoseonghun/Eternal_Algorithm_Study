N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  x, y = map(int, input().split())
  if y not in graph[x]:
    graph[x].append(y)
  if x not in graph[y]:
    graph[y].append(x)

dfs_visited = [False] * (N+1)
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in sorted(graph[v]):
    if not visited[i]:
      dfs(graph, i, visited)


bfs_visited = [False] * (N+1)
from collections import deque
def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in sorted(graph[v]):
      if not visited[i]:
        queue.append(i)
        visited[i] = True
dfs(graph, V, dfs_visited)
print()
bfs(graph, V, bfs_visited)
print()
