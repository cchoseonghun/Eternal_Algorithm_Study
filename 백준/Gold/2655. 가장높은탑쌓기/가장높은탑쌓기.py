N = int(input())
arr = []
arr.append((0, 0, 0, 0))
for i in range(1, N + 1):
  A, H, W = map(int, input().split())
  arr.append((i, A, H, W))

arr.sort(key=lambda x: x[3])
dp = [0] * (N + 1)

for i in range(1, N + 1):
  for j in range(0, i):
    if arr[i][1] > arr[j][1]:
      dp[i] = max(dp[i], dp[j] + arr[i][2])

max_value = max(dp)
index = N
result = []

while index != 0:
  if max_value == dp[index]:
    result.append(arr[index][0])
    max_value -= arr[index][2]
  index -= 1

result.reverse()
print(len(result))
[print(i) for i in result]