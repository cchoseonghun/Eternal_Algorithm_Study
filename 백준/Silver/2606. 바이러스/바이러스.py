from collections import deque

def BFS(start):
  visited = [False] * (C+1)
  visited[start] = True
  queue = deque([start])
  count = -1
  while queue:
    v = queue.popleft()
    count += 1
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
  return count

C = int(input())
N = int(input())
graph = [[] for _ in range(C+1)]
for _ in range(N):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

print(BFS(1))