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

N = int(input())
board = [list(input()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
result = 0
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      DFS(i, j, board[i][j])
      result += 1

print(result, end=' ')

for i in range(N):
  for j in range(N):
    if board[i][j] == 'G':
      board[i][j] = 'R'

visited = [[False] * N for _ in range(N)]
result = 0
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      DFS(i, j, board[i][j])
      result += 1

print(result, end=' ')