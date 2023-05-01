N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
target_arr = list(map(int, input().split()))


def search(arr, target):
  start = 0
  end = N-1
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return 1
    elif arr[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return 0


for x in target_arr:
  print(search(arr, x))
