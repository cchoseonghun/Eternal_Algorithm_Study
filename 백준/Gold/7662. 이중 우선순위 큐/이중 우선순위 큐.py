import sys
input = sys.stdin.readline
import heapq

def pop(heap):
  while len(heap) > 0:
    data, id = heapq.heappop(heap)
    if not deleted[id]: 
      deleted[id] = True
      return data
  return None

for _ in range(int(input())):
  K = int(input())
  minheap = []
  maxheap = []
  index = 0
  deleted = [False] * (K + 1)
  for _ in range(K):
    command = input().split()
    operator, data = command[0], int(command[1])
    if operator == 'D':
      if data == -1:
        pop(minheap)
      elif data == 1:
        pop(maxheap)
    elif operator == 'I':
      heapq.heappush(minheap, (data, index))
      heapq.heappush(maxheap, (-data, index))
      index += 1
  max_value = pop(maxheap)
  if max_value == None:
    print('EMPTY')
  else:
    heapq.heappush(minheap, (-max_value, index))
    print(-max_value, pop(minheap))