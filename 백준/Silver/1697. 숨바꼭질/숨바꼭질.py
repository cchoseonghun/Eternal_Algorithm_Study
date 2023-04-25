from collections import deque

N, K = map(int, input().split())
distance = [0] * 100001

queue = deque([N])
while queue:
  v = queue.popleft()
  if v == K:
    print(distance[v])
    break
  for i in (v-1, v+1, v*2):
    if 0 <= i <= 100000 and distance[i] == 0:
      distance[i] = distance[v] + 1
      queue.append(i)