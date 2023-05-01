N = int(input())
arr = set(map(int, input().split()))
M = int(input())
target_arr = list(map(int, input().split()))


for target in target_arr:
  if target not in arr:
    print(0)
  else:
    print(1)
