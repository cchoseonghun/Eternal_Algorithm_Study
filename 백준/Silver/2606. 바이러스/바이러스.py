computer = int(input())
connect = int(input())
graph = [[] for _ in range(computer+1)]

for _ in range(connect):
  x, y = map(int, input().split())
  if y not in graph[x]:
    graph[x].append(y)
  if x not in graph[y]:
    graph[y].append(x)

visited = [False] * (computer + 1)
count = 0
def dfs(graph, v, visited):
  global count
  visited[v] = True
  count += 1
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
dfs(graph, 1, visited)
print(count - 1)