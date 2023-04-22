import sys
up, down = True, True
arr = list(map(int, sys.stdin.readline().split()))
for i in range(1, len(arr)):
  if arr[i] > arr[i-1]:
    down = False
  else:
    up = False

if up:
  print('ascending')
elif down:
  print('descending')
else:
  print('mixed')