N = int(input())
arr = list(map(int, input().split()))
stack = []
for i in range(len(arr)):
  stack.append((arr[i], i+1))
result = []

def turn_left(stack):
  stack.append(stack.pop(0))

def turn_right(stack):
  stack.insert(0, stack.pop())

target, index = stack.pop(0)
result.append(index)

while len(stack) > 0:
  if target > 0:
    for _ in range(abs(target)-1):
      turn_left(stack)
  else:
    for _ in range(abs(target)):
      turn_right(stack)
  target, index = stack.pop(0)
  result.append(index)

for x in result:
  print(x, end=' ')
