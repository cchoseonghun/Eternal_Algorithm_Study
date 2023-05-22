import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
  x, y = map(int, input().split())
  arr.append((x, y))
arr.sort()

result = 0
start, current = arr[0]
for line in arr:
  x, y = line
  if x <= current:
    current = max(current, y)
  else:
    result += current - start
    start = x
    current = y
result += current - start

print(result)