from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n, d, c = map(int, input().split())
  graph = defaultdict(list)
  distances = defaultdict(list)
  for _ in range(d):
    a, b, s = map(int, input().split())
    graph[b].append((s, a))
    distances[a] = 1e9
    distances[b] = 1e9
  distances[c] = 0

  queue = []
  heapq.heappush(queue, (0, c))
  while queue:
    curr_d, curr_n = heapq.heappop(queue)
    if distances[curr_n] < curr_d:
      continue
    for next_d, next_n in graph[curr_n]:
      new_d = curr_d + next_d
      if new_d < distances[next_n]:
        distances[next_n] = new_d
        heapq.heappush(queue, (new_d, next_n))

  count = 0
  m = 0
  for x in distances.values():
    if x != 1e9:
      count += 1
      m = max(m, x)
  print(count, m)