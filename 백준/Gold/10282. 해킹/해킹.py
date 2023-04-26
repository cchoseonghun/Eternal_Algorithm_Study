import heapq

def dijkstra(start):
  distances = [float('inf')] * (n+1)
  distances[start] = 0
  queue = []
  heapq.heappush(queue, (0, start))

  while queue:
    curr_distance, curr_node = heapq.heappop(queue)
    if distances[curr_node] < curr_distance:
      continue
    for n_distance, n_node in graph[curr_node]:
      distance = curr_distance + n_distance
      if distance < distances[n_node]:
        distances[n_node] = distance
        heapq.heappush(queue, (distance, n_node))
  return distances

for _ in range(int(input())):
  n, d, c = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  for _ in range(d):
    a, b, s = map(int, input().split())
    graph[b].append((s, a))  # (distance, node)
  
  result = dijkstra(c)

  count = 0
  max_distance = 0
  for x in result:
    if x != float('inf'):
      count += 1
      max_distance = max(max_distance, x)
  print(count, max_distance)