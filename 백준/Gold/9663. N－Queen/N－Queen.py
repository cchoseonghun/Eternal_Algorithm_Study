def is_available(candidate, curr_col):
  curr_row = len(candidate)
  for queen_row in range(curr_row):
    if candidate[queen_row] == curr_col or abs(curr_col - candidate[queen_row]) == curr_row - queen_row:
      return False
  return True

def dfs(N, candidate, result):
  if len(candidate) == N:
    result.append([*candidate])
    return
  for curr_col in range(N):
    if is_available(candidate, curr_col):
      candidate.append(curr_col)
      dfs(N, candidate, result)
      candidate.pop()

N = int(input())
result = []
dfs(N, [], result)
print(len(result))