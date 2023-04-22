N, M = map(int, input().split())
n = list(map(int, input().split()))
r = 3

result = [0] * r
sum_arr = []
def ncr(L, start):
  if L == r:
    sum_result = sum(result)
    if sum_result <= M:
      sum_arr.append(sum_result)
  else:
    for i in range(start, len(n)):
      result[L] = n[i]
      ncr(L + 1, i + 1)

ncr(0, 0)
print(max(sum_arr))