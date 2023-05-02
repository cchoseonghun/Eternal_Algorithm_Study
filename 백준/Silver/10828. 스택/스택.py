import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input().strip())):
  command = input().strip()
  if 'push' in command:
    s, x = command.split()
    stack.append(int(x))
  elif 'pop' == command:
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  elif 'size' == command:
    print(len(stack))
  elif 'empty' == command:
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif 'top' == command:
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])