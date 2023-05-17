import heapq

N, M = map(int, input().split())
arr = list(map(int, input().split()))

largest = max(max(arr), -min(arr))

positive = []
negative = []

for x in arr:
  if x > 0:
    heapq.heappush(positive, -x)
  else:
    heapq.heappush(negative, x)

result = 0

while positive:
  result += heapq.heappop(positive)
  for _ in range(M - 1):
    if positive:
      heapq.heappop(positive)

while negative:
  result += heapq.heappop(negative)
  for _ in range(M - 1):
    if negative:
      heapq.heappop(negative)

result = -result * 2 - largest
print(result)