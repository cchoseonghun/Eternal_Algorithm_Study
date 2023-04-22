from collections import deque
def solution(maps):
  def bfs(y, x):
    q = deque()
    q.append((y, x, 1))
    while q:
      y, x, distance = q.popleft()  # distance: 총 지나온 거리

      if y == len(maps)-1 and x == len(maps[0])-1:  # 탈출
        return distance
      
      if maps[y][x] == 0:
        continue

      maps[y][x] = 0  # 지나온 길은 다시 안가게끔 0 처리
      if y+1 < len(maps):  # 아래
        q.append((y+1, x, distance+1))

      if x+1 < len(maps[0]):  # 우측
        q.append((y, x+1, distance+1))

      if y-1 >= 0:  # 위
        q.append((y-1, x, distance+1))

      if x-1 >= 0:  # 좌측
        q.append((y, x-1, distance+1))

    return -1  # 다 돌았음에도 탈출하지 못할 시 -1 리턴
  
  return bfs(0, 0)