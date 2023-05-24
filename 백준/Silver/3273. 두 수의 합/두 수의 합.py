N = int(input())
arr = list(map(int, input().split()))
target = int(input())
arr.sort()

i = 0
j = N - 1
result = 0

while i < j:
  check = arr[i] + arr[j]
  if check < target:
    i += 1
  else:
    if check == target:
      result += 1
    j -= 1

print(result)