import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
  visited[x][y] = True
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  for dx, dy in directions:
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
      continue
    if field[nx][ny] and not visited[nx][ny]:
      dfs(nx, ny)

for _ in range(int(input())):
  M, N, K = map(int, input().split())
  field = [[0] * M for _ in range(N)]
  visited = [[False] * M for _ in range(N)]
  for _ in range(K):
    y, x = map(int, input().split())
    field[x][y] = 1

  result = 0
  for x in range(N):
    for y in range(M):
      if field[x][y] and not visited[x][y]:
        dfs(x, y)
        result += 1
  print(result)