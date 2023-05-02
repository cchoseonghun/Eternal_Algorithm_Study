def find(x):
  if x == parent[x]:
    return x
  else:
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x != y:
    parent[y] = x
    count[x] += count[y]

for _ in range(int(input())):
  F = int(input())
  parent, count = {}, {}
  for _ in range(F):
    x, y = input().split()

    if x not in parent:
      parent[x] = x
      count[x] = 1
    if y not in parent:
      parent[y] = y
      count[y] = 1
    union(x, y)
    print(count[find(x)])
