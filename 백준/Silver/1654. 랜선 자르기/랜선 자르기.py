import sys
input = sys.stdin.readline

def solution(arr):
  start = 1
  end = max(arr)
  result = 0
  while start <= end:
    mid = (start + end) // 2
    count = 0
    for lan in arr:
      total = mid
      while total <= lan:
        count += 1
        total += mid
    if count >= N:
      result = mid
      start = mid + 1
    else:
      end = mid - 1
  return result

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
print(solution(arr))