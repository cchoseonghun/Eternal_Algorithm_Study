import heapq

for _ in range(int(input())):
  K = int(input())
  minheap = []
  maxheap = []
  deleted = []

  index = 0
  for _ in range(K):
    command, n = input().split()
    if command == 'I':
      heapq.heappush(minheap, (int(n), index))
      heapq.heappush(maxheap, (-int(n), index))
      deleted.append(False)
      index += 1
    elif command == 'D':
      if int(n) > 0:
        while len(maxheap) > 0:
          x, i = heapq.heappop(maxheap)
          if not deleted[i]:
            deleted[i] = True
            break
      if int(n) < 0:
        while len(minheap) > 0:
          x, i = heapq.heappop(minheap)
          if not deleted[i]:
            deleted[i] = True
            break

  if deleted.count(True) == len(deleted):
    print('EMPTY')
  else:
    while True:
      x, i = heapq.heappop(maxheap)
      if not deleted[i]:
        print(-x, end=' ')
        break
    while True:
      x, i = heapq.heappop(minheap)
      if not deleted[i]:
        print(x, end=' ')
        break