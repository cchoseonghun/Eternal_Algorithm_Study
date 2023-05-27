import sys
input = sys.stdin.readline
import heapq
from collections import deque

def daijkstra():
  distances[S] = 0
  heap = []
  heapq.heappush(heap, (0, S))
  while heap:
    curr_d, curr_n = heapq.heappop(heap)
    if distances[curr_n] < curr_d:
      continue
    for next_d, next_n in graph[curr_n]:
      new_d = curr_d + next_d
      if new_d < distances[next_n] and not visited[curr_n][next_n]:
        distances[next_n] = new_d
        heapq.heappush(heap, (new_d, next_n))

def BFS():
  queue = deque([D])
  while queue:
    curr_n = queue.popleft()
    for prev_d, prev_n in r_graph[curr_n]:
      if distances[curr_n] == distances[prev_n] + prev_d and not visited[prev_n][curr_n]:
        visited[prev_n][curr_n] = True
        queue.append(prev_n)
        
while True:
  N, M = map(int, input().split())
  if N == 0 and M == 0:
    exit()
  S, D = map(int, input().split())
  graph = [[] for _ in range(N)]
  r_graph = [[] for _ in range(N)]
  visited = [[False] * N for _ in range(N)]
  distances = [1e9] * N

  for _ in range(M):
    U, V, P = map(int, input().split())
    graph[U].append((P, V))
    r_graph[V].append((P, U))

  daijkstra()
  BFS()
  distances = [1e9] * N
  daijkstra()

  result = distances[D]
  if result == 1e9:
    print(-1)
  else:
    print(result)
