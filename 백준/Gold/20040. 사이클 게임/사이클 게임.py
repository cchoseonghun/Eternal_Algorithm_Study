import sys
input = sys.stdin.readline

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x < y:
    parent[y] = x
  else:
    parent[x] = y

n, m = map(int, input().split())
parent = [0] * n
for i in range(n):
  parent[i] = i

cycle = False
for i in range(m):
  x, y = map(int, input().split())
  if find(x) == find(y):
    cycle = True
    print(i + 1)
    break
  else:
    union(x, y)
if not cycle:
  print(0)