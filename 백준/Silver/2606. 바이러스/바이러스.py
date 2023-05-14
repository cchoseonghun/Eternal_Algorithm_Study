def DFS(v, visited):
  global x
  visited[v] = True
  x += 1
  for i in graph[v]:
    if not visited[i]:
      DFS(i, visited)

C = int(input())
N = int(input())
graph = [[] for _ in range(C+1)]
for _ in range(N):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

x = -1
visited = [False] * (C+1)
DFS(1, visited)
print(x)