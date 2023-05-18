from itertools import combinations

check = ['a', 'e', 'i', 'o', 'u']

def is_available(target):
  count = 0
  for x in target:
    if x in check:
      count += 1
  if 1 <= count <= R - 2:
    return True
  return False

R, C = map(int, input().split())
arr = list(input().split())
arr.sort()
for x in combinations(arr, R):
  if is_available(x):
    print(''.join(x))