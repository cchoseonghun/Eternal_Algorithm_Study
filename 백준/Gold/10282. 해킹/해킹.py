import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  N, D, C = map(int, input().split())
  graph = defaultdict(list)
  d = {}
  for _ in range(D):
    a, b, s = map(int, input().split())
    if b not in graph:
      graph[b] = [(s, a)]
    else:
      graph[b].append((s, a))

    if a not in d:
      d[a] = 1e9
    if b not in d:
      d[b] = 1e9
  d[C] = 0

  queue = []
  heapq.heappush(queue, (0, C))
  while queue:
    curr_d, curr_n = heapq.heappop(queue)
    if d[curr_n] < curr_d:
      continue
    for next_d, next_n in graph[curr_n]:
      new_d = curr_d + next_d
      if new_d < d[next_n]:
        d[next_n] = new_d
        heapq.heappush(queue, (new_d, next_n))

  count = 0
  m = 0
  for _, distance in d.items():
    if distance != 1e9:
      count += 1
      m = max(m, distance)
  print(count, m)