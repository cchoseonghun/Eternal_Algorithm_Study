arr = []
for _ in range(int(input())):
  age, name = input().split()
  arr.append((int(age), name))
arr.sort(key=lambda x: x[0])
for age, name in arr:
  print(age, name)