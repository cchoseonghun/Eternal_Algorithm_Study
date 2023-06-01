from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y, maps):
    n = len(maps)
    m = len(maps[0])
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1

def solution(maps):
    BFS(0, 0, maps)
    result = maps[-1][-1]
    if result == 1:
        return -1
    else:
        return result
    
    