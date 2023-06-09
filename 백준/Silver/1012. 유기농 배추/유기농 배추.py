import sys
sys.setrecursionlimit(100000)

def dfs(y, x):
  if x < 0 or x >= M or y < 0 or y >= N:
    return False
  if field[y][x] == 1:
    field[y][x] = 0
    dfs(y+1, x)
    dfs(y, x+1)
    dfs(y-1, x)
    dfs(y, x-1)
    return True
  else:
    return False
    
for _ in range(int(input())):
  M, N, K = map(int, input().split())
  field = [[0] * M for _ in range(N)]
  for _ in range(K):
    x, y = map(int, input().split())
    field[y][x] = 1

  count = 0
  for y in range(N):
    for x in range(M):
      if dfs(y, x):
        count += 1
  print(count)
