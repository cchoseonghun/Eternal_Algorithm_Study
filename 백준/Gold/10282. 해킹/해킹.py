import heapq

for _ in range(int(input())):
  n, d, c = map(int, input().split())
  graph = { computer: {} for computer in range(1, n+1) }
  for _ in range(d):
    a, b, s = map(int, input().split())
    graph[b][a] = s

  def dijkstra(graph, start):
    distances = { node: float('inf') for node in graph }
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
      curr_distance, curr_node = heapq.heappop(queue)

      if distances[curr_node] < curr_distance:
        continue

      for n_node, n_distance in graph[curr_node].items():
        distance = curr_distance + n_distance
        if distance < distances[n_node]:
          distances[n_node] = distance
          heapq.heappush(queue, [distance, n_node])
    
    return distances

  result = dijkstra(graph, c)

  count = 0
  max_distance = 0
  for i in result:
    if result[i] != float('inf'):
      count += 1
      max_distance = max(max_distance, result[i])
  print(count, max_distance)