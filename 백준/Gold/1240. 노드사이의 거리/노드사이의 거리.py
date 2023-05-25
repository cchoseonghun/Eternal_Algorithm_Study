import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def DFS(v, target, result):
  visited[v] = True
  if v == target:
    print(result)
    return
  for d, i in graph[v]:
    if not visited[i]:
      DFS(i, target, result + d)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
  x, y, d = map(int, input().split())
  graph[x].append((d, y))
  graph[y].append((d, x))

for _ in range(M):
  start, end = map(int, input().split())
  visited = [False] * (N + 1)
  DFS(start, end, 0)