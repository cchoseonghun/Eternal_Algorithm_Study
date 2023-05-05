# 1. 첫번째 원소 뽑아내기
# 2. 왼쪽으로 회전
# 3. 오른쪽으로 회전

N, M = map(int, input().split())
arr = [x for x in range(1, N+1)]
target_arr = list(map(int, input().split()))  # len(target_arr) = M

count = 0

def pop_first(arr):
  return arr.pop(0)

def turn_left(arr, target, count):
  if arr[0] == target:
    return count
  arr.append(arr.pop(0))
  return turn_left(arr, target, count + 1)

def turn_right(arr, target, count):
  if arr[0] == target:
    return count
  arr.insert(0, arr.pop())
  return turn_right(arr, target, count + 1)

for target in target_arr:
  x = turn_left([*arr], target, 0)
  y = turn_right([*arr], target, 0)
  if x < y:
    count = turn_left(arr, target, count)
  else:
    count = turn_right(arr, target, count)
  pop_first(arr)
print(count)