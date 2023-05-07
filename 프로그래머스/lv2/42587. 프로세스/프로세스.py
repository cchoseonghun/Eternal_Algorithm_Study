from collections import deque
def solution(priorities, location):
    queue = deque()
    for i, x in enumerate(priorities):
        queue.append((x, i))
    count = 1
    while queue:
        m = max(queue, key=lambda item: item[0])[0]
        x, i = queue.popleft()
        if x >= m:
            if i == location:
                return count
            else:
                count += 1
        else:
            queue.append((x, i))