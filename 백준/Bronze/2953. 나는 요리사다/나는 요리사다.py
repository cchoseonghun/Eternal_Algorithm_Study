arr = []
for i in range(5):
  score = sum(list(map(int, input().split())))
  arr.append((i+1, score))

x, y = max(arr, key=lambda x: x[1])
print(x, y)