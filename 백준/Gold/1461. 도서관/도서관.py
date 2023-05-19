import heapq

N, M = map(int, input().split())
arr = list(map(int, input().split()))

positive = []
negative = []

largest = max(max(arr), -min(arr))

for x in arr:
  if x < 0:
    heapq.heappush(negative, x)
  else:
    heapq.heappush(positive, -x)

result = 0
while negative:
  result += heapq.heappop(negative)
  for _ in range(M - 1):
    if negative:
      heapq.heappop(negative)
while positive:
  result += heapq.heappop(positive)
  for _ in range(M - 1):
    if positive:
      heapq.heappop(positive)
print(result * 2 * -1 - largest)