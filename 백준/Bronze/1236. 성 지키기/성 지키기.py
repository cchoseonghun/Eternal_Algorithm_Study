N, M = map(int, input().split())
count = 0
arr = [0] * M
for _ in range(N):
  row = input()
  if row.count('X') == 0:
    count += 1
  for i, x in enumerate(row):
    if x == 'X':
      arr[i] += 1
print(max(count, arr.count(0)))