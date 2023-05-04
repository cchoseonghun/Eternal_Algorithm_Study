import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip().split()))
stack = []
NGE = [-1] * N

for i in range(N):
  x = arr[i]
  if len(stack) == 0 or stack[-1][0] >= x:
    stack.append((x, i))
  else:
    while len(stack) > 0:
      pre, index = stack.pop()
      if pre >= x:
        stack.append((pre, index))
        break
      else:
        NGE[index] = x
    stack.append((x, i))

for x in NGE:
  print(x, end=' ')