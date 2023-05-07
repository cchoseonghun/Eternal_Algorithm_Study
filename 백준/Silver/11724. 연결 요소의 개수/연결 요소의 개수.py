import sys
input = sys.stdin.readline

def find(x):
  if x != parent[x]:
    parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x < y:
    parent[y] = x
  else:
    parent[x] = y

def make_set(x):
  if x not in parent:
    parent[x] = x
    rank[x] = 0

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
  x, y = map(int, input().split())
  union(x, y)

for i in range(len(parent)):
  find(i)
print(len(list(set(parent))) - 1)