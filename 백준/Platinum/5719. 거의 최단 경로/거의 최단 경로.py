from collections import deque
import heapq
import sys
input = sys.stdin.readline

def dijkstra():
  queue = []
  heapq.heappush(queue, (0, S))
  distances[S] = 0
  while queue:
    curr_d, curr_n = heapq.heappop(queue)
    if distances[curr_n] < curr_d:
      continue
    for next_d, next_n in graph[curr_n]:
      new_d = curr_d + next_d
      if new_d < distances[next_n] and not dropped[curr_n][next_n]:
        distances[next_n] = new_d
        heapq.heappush(queue, (new_d, next_n))

def BFS():
  queue = deque([D])
  while queue:
    now = queue.popleft()
    if now == S:
      continue
    for cost, prev in reverse_graph[now]:
      if distances[now] == distances[prev] + cost and not dropped[prev][now]:
        dropped[prev][now] = True
        queue.append(prev)

while True:
  N, M = map(int, input().split())
  if N == 0 and M == 0:
    break
  graph = [[] for _ in range(N)]
  reverse_graph = [[] for _ in range(N)]

  S, D = map(int, input().split())
  for _ in range(M):
    U, V, P = map(int, input().split())
    graph[U].append((P, V))
    reverse_graph[V].append((P, U))

  dropped = [[False] * N for _ in range(N)]
  distances = [1e9] * N
  dijkstra()
  BFS()

  distances = [1e9] * (N)
  dijkstra()

  if distances[D] != 1e9:
    print(distances[D])
  else:
    print(-1)