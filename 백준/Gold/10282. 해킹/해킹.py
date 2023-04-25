import heapq

def dijkstra(start):
  distances[start] = 0
  queue = []
  heapq.heappush(queue, (0, start))

  while queue:
    curr_distance, curr_node = heapq.heappop(queue)

    if distances[curr_node] < curr_distance:
      continue

    for n_node, n_distance in graph[curr_node]:
      distance = curr_distance + n_distance
      if distances[n_node] > distance:
        distances[n_node] = distance
        heapq.heappush(queue, (distance, n_node))

for _ in range(int(input())):
  n, d, start = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  distances = [float('inf')] * (n+1)

  for _ in range(d):
    a, b, s = map(int, input().split())
    graph[b].append((a, s))

  dijkstra(start)

  count = 0
  max_distance = 0
  for i in distances:
    if i != float('inf'):
      count += 1
      max_distance = max(max_distance, i)
  print(count, max_distance)