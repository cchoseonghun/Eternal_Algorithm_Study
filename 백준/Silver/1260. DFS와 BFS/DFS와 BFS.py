from collections import deque

def DFS(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      DFS(graph, i, visited)

def BFS(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

for x in graph:
  x.sort()

visited = [False] * (N+1)
DFS(graph, V, visited)
print()
visited = [False] * (N+1)
BFS(graph, V, visited)