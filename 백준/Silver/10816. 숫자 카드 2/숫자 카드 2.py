import sys
input = sys.stdin.readline

def left(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if (mid == 0 or arr[mid-1] < target) and arr[mid] == target:
      return mid
    elif arr[mid] >= target:
      end = mid - 1
    else:
      start = mid + 1
  return None

def right(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if (mid == N-1 or arr[mid+1] > target) and arr[mid] == target:
      return mid
    elif arr[mid] <= target:
      start = mid + 1
    else:
      end = mid - 1
  return None

def solution(cards, target):
  start = left(cards, target, 0, N-1)
  end = right(cards, target, 0, N-1)
  if start is None or end is None:
    return 0
  return end - start + 1

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
target_arr = list(map(int, input().split()))

for x in target_arr:
  print(solution(cards, x), end=' ')