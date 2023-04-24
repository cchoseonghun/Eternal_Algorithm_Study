from collections import deque

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  x, y = map(int, input().split())
  graph[x].append(y)

distance = [-1] * (N+1)
distance[X] = 0

queue = deque()
queue.append(X)

while queue:
  v = queue.popleft()
  for i in graph[v]:
    if distance[i] == -1:
      distance[i] = distance[v] + 1
      queue.append(i)

check = False
for i, x in enumerate(distance):
  if x == K:
    check = True
    print(i)

if check == False:
  print(-1)