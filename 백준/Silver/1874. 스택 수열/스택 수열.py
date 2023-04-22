# 출력: push, pop 연산을 출력. push: +, pop: -
# 조건을 만족할 수 없을 시 'NO' 출력

# 조건:
# 첫째줄 n (1 ≤ n ≤ 100,000)
# 1 <= arr[i] <= n

n = int(input())

count = 1
stack = []
result = []

for _ in range(n):
  data = int(input())
  while count <= data:
    stack.append(count)
    count += 1
    result.append('+')
  if stack[-1] == data:
    stack.pop()
    result.append('-')
  else:
    print('NO')
    exit(0)

print('\n'.join(result))