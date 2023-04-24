n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  x, y = map(int, input().split())
  if y not in graph[x]:
    graph[x].append(y)
  if x not in graph[y]:
    graph[y].append(x)

visited = [False] * (n+1)
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in sorted(graph[v]):
    if not visited[i]:
      dfs(graph, i, visited)

dfs(graph, v, visited)
print()

visited = [False] * (n+1)
from collections import deque
def bfs(graph, start, visited):
  queue = deque()
  queue.append(start)
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in sorted(graph[v]):
      if not visited[i]:
        queue.append(i)
        visited[i] = True
bfs(graph, v, visited)
