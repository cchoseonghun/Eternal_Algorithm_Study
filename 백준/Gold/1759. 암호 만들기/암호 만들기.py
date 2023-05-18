def nCr(level, start):
  if level == L:
    if check(result):
      print(''.join(result))
  else:
    for i in range(start, len(arr)):
      result[level] = arr[i]
      nCr(level + 1, i + 1)

def check(target):
  count = 0
  for x in target:
    if x in M:
      count += 1
  if 1 <= count <= L - 2:
    return True
  else:
    return False

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
M = ['a', 'e', 'i', 'o', 'u']
result = [0] * L
nCr(0, 0)