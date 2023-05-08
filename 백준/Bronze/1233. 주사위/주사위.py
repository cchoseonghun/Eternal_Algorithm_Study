s1, s2, s3 = map(int, input().split())
counter = {}

for i in range(1, s1 + 1):
  for j in range(1, s2 + 1):
    for k in range(1, s3 + 1):
      summary = i + j + k
      if summary not in counter:
        counter[summary] = 1
      else:
        counter[summary] += 1

max_count = -1
answer = int(1e9)
for key, value in counter.items():
  if max_count < value:
    max_count = value
    answer = key
  elif max_count == value:
    answer = min(answer, key)

print(answer)