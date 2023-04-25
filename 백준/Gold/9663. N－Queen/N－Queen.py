def is_available(x):
  for i in range(x):
    if row[x] == row[i]:
      return False
    if abs(row[x] - row[i]) == x - i:
      return False
  return True

def DFS(x):
  global result
  if x == N:
    result += 1
  else:
    for i in range(N):
      row[x] = i
      if is_available(x):
        DFS(x+1)

N = int(input())
row = [0] * N
result = 0
DFS(0)
print(result)