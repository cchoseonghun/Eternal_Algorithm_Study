def DFS(x, y):
  if board[x][y] == 0:
    return
  else:
    global temp
    board[x][y] = 0
    temp += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1:
        DFS(nx, ny)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
board = []
for _ in range(N):
  arr = [int(x) for x in input()]
  board.append(arr)

result = []
for i in range(N):
  for j in range(N):
    if board[i][j] != 0:
      temp = 0
      DFS(i, j)
      result.append(temp)

result.sort()
print(len(result))
for x in result:
  print(x)
