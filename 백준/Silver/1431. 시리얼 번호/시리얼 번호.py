def get_num_sum(target):
  result = 0
  for x in target:
    if ord(x) < 65:
      result += int(x)
  return result

N = int(input())
arr = [input() for _ in range(N)]

arr.sort(key=lambda x: (len(x), get_num_sum(x), x))
[print(x, end=' ') for x in arr]