N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)
result = 0
while start <= end:
  mid = (start + end) // 2
  count = 1
  b = 0
  for x in arr:
    if b + x <= mid:
      b += x
    else:
      count += 1
      b = x
  if count <= M:
    end = mid - 1
    result = mid
  else:
    start = mid + 1
print(result)