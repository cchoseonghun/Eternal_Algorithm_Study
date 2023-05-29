import sys
input = sys.stdin.readline
import heapq

for _ in range(int(input())):
  arr = []
  M = int(input())
  for _ in range(M // 10 + 1):
    temp = list(map(int, input().split()))
    arr.extend(temp)
  left = []
  right = []
  mid = 0
  result = []
  for i, x in enumerate(arr):
    if i == 0:
      mid = x
    else:
      if mid < x:
        heapq.heappush(right, x)
      else:
        heapq.heappush(left, -x)
    if i % 2 == 0:
      if len(left) < len(right):
        heapq.heappush(left, -mid)
        mid = heapq.heappop(right)
      elif len(left) > len(right):
        heapq.heappush(right, mid)
        mid = -heapq.heappop(left)
      result.append(mid)
  print(len(result))
  for i, x in enumerate(result):
    if i >= 10 and i % 10 == 0:
      print()
    print(x, end=' ')
  print()
    