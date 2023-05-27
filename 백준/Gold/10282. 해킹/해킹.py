import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  N, D, C = map(int, input().split())
  graph = [[] for _ in range(N + 1)]
  distances = [1e9] * (N + 1)
  distances[C] = 0
  for _ in range(D):
    a, b, s = map(int, input().split())
    graph[b].append((s, a))

  heap = []
  heapq.heappush(heap, (0, C))
  while heap:
    curr_d, curr_n = heapq.heappop(heap)
    if distances[curr_n] < curr_d:
      continue
    for next_d, next_n in graph[curr_n]:
      new_d = curr_d + next_d
      if new_d < distances[next_n]:
        distances[next_n] = new_d
        heapq.heappush(heap, (new_d, next_n))

  count = 0
  timer = 0
  for x in distances:
    if x != 1e9:
      count += 1
      timer = max(timer, x)
  print(count, timer)