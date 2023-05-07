import sys
input = sys.stdin.readline

def find(x):
  if x != parent[x]:
    parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x == y:
    return True
  else:
    if rank[x] < rank[y]:
      parent[x] = y
    else:
      parent[y] = x
      if rank[x] == rank[y]:
        rank[x] += 1
    return False

def make_set(x):
  if x not in parent:
    parent[x] = x
    rank[x] = 0

n, m = map(int, input().split())
parent, rank = {}, {}
count = 1
for _ in range(m):
  x, y = map(int, input().split())
  make_set(x)
  make_set(y)
  if union(x, y):
    print(count)
    exit()
  else:
    count += 1
print(0)