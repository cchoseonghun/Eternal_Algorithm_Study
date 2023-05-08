arr = [-1] * 26
S = input()
for i in range(len(S)):
  index = ord(S[i]) - ord('a')
  if arr[index] == -1:
    arr[index] = i
for x in arr:
  print(x, end=' ')