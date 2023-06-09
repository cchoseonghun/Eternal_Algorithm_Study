import sys
input = sys.stdin.readline

def DFS(x, y):
  result = 1
  board[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1:
      result += DFS(nx, ny)
  return result

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
board = [[0] * N for _ in range(N)]
for i in range(N):
  row = input()
  for j in range(N):
    board[i][j] = int(row[j])

result = []
for i in range(N):
  for j in range(N):
    if board[i][j] == 1:
      result.append(DFS(i, j))

result.sort()
print(len(result))
for x in result:
  print(x)
