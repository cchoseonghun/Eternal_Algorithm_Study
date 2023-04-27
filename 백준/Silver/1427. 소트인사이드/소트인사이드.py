N = input()
for i in range(9, -1, -1):
  for j in N:
    if int(j) == i:
      print(i, end='')