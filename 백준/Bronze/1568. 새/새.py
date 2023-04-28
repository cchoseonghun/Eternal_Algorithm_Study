N = int(input())
check = 1
result = 0
while N > 0:
  if N >= check:
    N -= check
    result += 1
    check += 1
  else:
    check = 1
print(result)