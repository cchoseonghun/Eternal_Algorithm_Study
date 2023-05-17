dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BFS(x, y):
  result = 0
  candidate = set()
  candidate.add((x, y, board[y][x]))
  while candidate:
    x, y, step = candidate.pop()
    result = max(result, len(step))
    
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if (0 <= ny < R and 0 <= nx < C and board[ny][nx] not in step):
        candidate.add((nx, ny, step + board[ny][nx]))
  return result

R, C = map(int, input().split())
board = []
for _ in range(R):
  board.append(input())

print(BFS(0, 0))