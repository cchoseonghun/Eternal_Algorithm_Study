import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(x, y, target):
  visited[x][y] = True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == target:
      DFS(nx, ny, target)

def DFS2(x, y, target):
  visited2[x][y] = True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < N and not visited2[nx][ny]:
      if (target == 'R' or target == 'G') and (board[nx][ny] == 'R' or board[nx][ny] == 'G'):
        DFS2(nx, ny, target)
      elif target == 'B' and board[nx][ny] == target:
        DFS2(nx, ny, target)

N = int(input())
board = [list(input()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]
result = 0
result2 = 0
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      DFS(i, j, board[i][j])
      result += 1
    if not visited2[i][j]:
      DFS2(i, j, board[i][j])
      result2 += 1
print(result, result2)