from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  x, y = map(int, input().split())
  graph[y].append(x)

def bfs(start):
  visited = [False] * (N+1)
  queue = deque([start])
  visited[start] = True
  count = 1
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        count += 1
  return count

max_count = 0
result = []
for i in range(1, N+1):
  count = bfs(i)
  if max_count < count:
    max_count = count
    result = [i]
  elif max_count == count:
    result.append(i)

for x in result:
  print(x, end=' ')