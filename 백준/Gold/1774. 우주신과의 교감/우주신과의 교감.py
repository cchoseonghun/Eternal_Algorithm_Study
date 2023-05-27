import sys
input = sys.stdin.readline

def get_distance(a, b):
  return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def find(n):
  if parent[n] != n:
    parent[n] = find(parent[n])
  return parent[n]

def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    if a < b:
      parent[b] = a
    else:
      parent[a] = b
    return True
  return False

edges = []
parent = {}
locations = []
N, M = map(int, input().split())

for _ in range(N):
  x, y = map(int, input().split())
  locations.append((x, y))

length = len(locations)

for i in range(length - 1):
  for j in range(i + 1, length):
    edges.append((i + 1, j + 1, get_distance(locations[i], locations[j])))

for i in range(1, N + 1):
  parent[i] = i

for i in range(M):
  a, b = map(int, input().split())
  union(a, b)

edges.sort(key=lambda data: data[2])

result = 0
for a, b, cost in edges:
  if union(a, b):
    result += cost

print('%0.2f'%result)