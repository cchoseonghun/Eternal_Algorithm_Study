N = int(input())
K = int(input())
arr = list(map(int, input().split()))

if N <= K:
  print(0)
  exit()

arr.sort()

distances = []
for i in range(N - 1):
  distances.append(arr[i + 1] - arr[i])
distances.sort()

for _ in range(K - 1):
  distances.pop()

print(sum(distances))