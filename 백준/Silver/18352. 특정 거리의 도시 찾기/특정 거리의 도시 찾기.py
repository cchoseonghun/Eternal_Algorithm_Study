from collections import deque

N, M, K, X = map(int, input().split())
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
# 2 ≤ N ≤ 300,000
# 1 ≤ M ≤ 1,000,000
# 1 ≤ K ≤ 300,000
# 1 ≤ X ≤ N

graph = [[] for _ in range(N+1)]
for _ in range(M):
  x, y = map(int, input().split())
  graph[x].append(y)
    
distance = [-1] * (N+1)
distance[X] = 0

queue = deque([X])
while queue:
  v = queue.popleft()
  for i in graph[v]:
    if distance[i] == -1:
      distance[i] = distance[v] + 1
      queue.append(i)

check = False
for i in range(1, N + 1):
  if distance[i] == K:
    print(i)
    check = True
if check == False:
  print(-1)