import heapq
import sys
input = sys.stdin.readline

def get_distance(a, b):
  return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x != y:
    if rank[x] < rank[y]:
      parent[x] = y
    else:
      parent[y] = x
      if rank[x] == rank[y]:
        rank[x] += 1
    return True
  return False

def make_set(x):
  parent[x] = x
  rank[x] = 0

def dijkstra(edges):
  mst = []
  while edges:
    edge = heapq.heappop(edges)
    _, (x, y) = edge
    if union(x, y):
      mst.append(edge)
  return mst

N, M = map(int, input().split())
edges = []
locations = []
parent = {}
rank = {}
for _ in range(N):
  x, y = map(int, input().split())
  locations.append((x, y))
for i in range(1, N + 1):
  for j in range(i + 1, N + 1):
    heapq.heappush(edges, (get_distance(locations[i-1], locations[j-1]), (i, j)))
    make_set(i)
    make_set(j)
for _ in range(M):
  x, y = map(int, input().split())
  union(x, y)

result = dijkstra(edges)
s = 0
for x, _ in result:
  s += x
print("%0.2f" % s)