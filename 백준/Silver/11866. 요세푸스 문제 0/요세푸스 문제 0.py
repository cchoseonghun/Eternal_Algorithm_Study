N, K = map(int, input().split())
arr = [x for x in range(1, N+1)]
result = []

while len(arr) > 0:
  for _ in range(K):
    arr.append(arr.pop(0))
  result.append(arr.pop())

print('<' + ', '.join(map(str, result)) + '>')