dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
  global answer
  answer = max(answer, cnt)
  visited[ord(board[x][y]) - ord('A')] = True

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < R and 0 <= ny < C and not visited[ord(board[nx][ny]) - ord('A')]:
      dfs(nx, ny, cnt + 1)

  visited[ord(board[x][y]) - ord('A')] = False

R, C = map(int, input().split())
board = [input() for _ in range(R)]
visited = [False] * 26

answer = 1
dfs(0, 0, 1)
print(answer)
