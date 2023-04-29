arr = []
for _ in range(int(input())):
  arr.append(int(input()))

high = 0
count = 1
for i in range(high+1, len(arr)):
  if arr[high] < arr[i]:
    high = i
    count += 1

print(count)

high = len(arr)-1
count = 1
for i in range(high-1, -1, -1):
  if arr[high] < arr[i]:
    high = i
    count += 1

print(count)
