import sys
input = sys.stdin.readline

def solution(trees, target, start, end):
  result = 0
  while start <= end:
    mid = (start + end) // 2
    total = 0
    for tree in trees:
      if mid < tree:
        total += tree - mid
    if total < target:
      end = mid - 1
    else:
      result = mid
      start = mid + 1
  return result

N, M = map(int, input().split())
trees = list(map(int, input().split()))
print(solution(trees, M, 0, max(trees)))