import sys
input = sys.stdin.readline
print = sys.stdout.write

arr = [0] * 10001
for _ in range(int(input())):
  arr[int(input())] += 1

for i, x in enumerate(arr):
  for _ in range(x):
    print(str(i)+'\n')