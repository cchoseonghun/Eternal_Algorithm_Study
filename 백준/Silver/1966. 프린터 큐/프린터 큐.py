case = int(input())  # 테스트케이스 개수

def solution():
  N, M = map(int, input().split())
  queue = list(map(int, input().split()))
  queue = [(i, value) for i, value in enumerate(queue)]

  count = 0
  while True:
    max_value = sorted(queue, key=lambda x: x[1], reverse=True)[0]
    if max_value == queue[0]:
      count += 1
      if queue.pop(0)[0] == M:
        print(count)
        break
    else:
      queue.append(queue.pop(0))

for i in range(case):
  solution()