import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
X = int(input())

start = 0
end = len(arr) - 1

result = 0
while start < end:
  target = arr[start] + arr[end]
  if target <= X:
    start += 1
    if target == X:
      result += 1
  else:
    end -= 1

print(result)