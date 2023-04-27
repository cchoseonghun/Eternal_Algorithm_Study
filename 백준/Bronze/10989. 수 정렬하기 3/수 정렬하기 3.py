import sys
N = int(sys.stdin.readline())

nums = [0]*10001
for _ in range(N):
  nums[int(sys.stdin.readline())] += 1

for idx in range(1,10001):
  for _ in range(nums[idx]):
      sys.stdout.write(str(idx)+'\n')