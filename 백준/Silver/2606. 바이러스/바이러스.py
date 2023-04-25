from collections import deque

computer = int(input())
connect = int(input())
graph = [[] for _ in range(computer+1)]
for _ in range(connect):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

count = -1
visited = [False] * (computer+1)

stack = deque([1])
visited[1] = True
while stack:
  v = stack.pop()
  count += 1
  for i in graph[v]:
    if not visited[i]:
      stack.append(i)
      visited[i] = True

print(count)