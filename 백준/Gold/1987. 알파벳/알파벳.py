def BFS(x, y):
  result = 0
  queue = set()
  queue.add((x, y, board[y][x]))

  while queue:
    cx, cy, candidate = queue.pop()
    result = max(result, len(candidate))
    for i in range(4):
      ny = cy + dy[i]
      nx = cx + dx[i]
      if (0 <= ny < R and 0 <= nx < C and board[ny][nx] not in candidate):
        queue.add((nx, ny, candidate + board[ny][nx]))

  return result


R, C = map(int, input().split())
board = []
for _ in range(R):
  board.append(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

print(BFS(0, 0))