# 상, 하, 좌, 우 방향으로 이동하기 위한 dx, dy 값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)  # 최댓값 갱신
    visited[ord(board[x][y]) - ord('A')] = True  # 방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited[ord(board[nx][ny]) - ord('A')]:
            dfs(nx, ny, cnt + 1)  # 이동하면서 카운트 증가

    visited[ord(board[x][y]) - ord('A')] = False  # 백트래킹

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
visited = [False] * 26  # 알파벳 방문 여부를 체크하기 위한 배열
answer = 1  # 최대 칸의 수 초기화

dfs(0, 0, 1)  # 시작 지점부터 DFS 탐색 시작

print(answer)
