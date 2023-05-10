import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while start <= end:
  mid = (start + end) // 2
  prev = arr[0]
  count = 1
  for x in arr:
    if prev + mid <= x:
      prev = x
      count += 1
  if count >= C:
    start = mid + 1
    result = mid
  else:
    end = mid - 1
    
print(result)