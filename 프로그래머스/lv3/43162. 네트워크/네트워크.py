from itertools import combinations

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x != y:
        parent[y] = x

def solution(n, computers):
    # union-find 로 네트워크 개수 확인
    # combinations를 통해 각 컴퓨터끼리의 연결을 computers[i][j] == 1로
    # 확인 후 연결되있다면 union 진행
    # 
    parent = [x for x in range(n)]
    for i, j in combinations(range(n), 2):
        if computers[i][j] == 1:
            union(parent, i, j)
    result = set()
    for i in range(n):
        result.add(find(parent, i))
    return len(result)
