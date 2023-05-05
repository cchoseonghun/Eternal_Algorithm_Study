import sys
input = sys.stdin.readline
import heapq
arr = []

for _ in range(int(input())):
  x = int(input())  
  if x != 0:
    heapq.heappush(arr, (abs(x), x))
  else:
    if len(arr) == 0:
      print(0)
    else:
      print(heapq.heappop(arr)[1])