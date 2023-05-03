import sys
input = sys.stdin.readline

counting = 1
arr = []
result = []
for _ in range(int(input())):
  k = int(input())
  while counting <= k:
    arr.append(counting)
    result.append('+')
    counting += 1
  if arr[-1] == k:
    arr.pop()
    result.append('-')
  else:
    print('NO')
    exit()
for x in result:
  print(x)