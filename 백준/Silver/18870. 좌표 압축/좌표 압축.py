N = int(input())
arr = list(map(int, input().split()))
unique = list(set(arr))
unique.sort()
target = {}
for i, x in enumerate(unique):
  target[x] = i
for x in arr:
  print(target[x], end=' ')
