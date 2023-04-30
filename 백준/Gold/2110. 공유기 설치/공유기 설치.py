import sys
input = sys.stdin.readline

def solution(arr, N, C):
  start = 1
  end = arr[-1] - arr[0]
  result = 0

  while start <= end:
    mid = (start + end) // 2
    prev = arr[0]
    count = 1
    for i in range(1, N):
      if arr[i] >= prev + mid:
        prev = arr[i]
        count += 1
    if count >= C:
      result = mid
      start = mid + 1
    else:
      end = mid - 1

  return result

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
print(solution(arr, N, C))