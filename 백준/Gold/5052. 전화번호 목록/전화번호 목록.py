for _ in range(int(input())):
  arr = []
  N = int(input())
  for _ in range(N):
    arr.append(input())

  arr.sort()
  
  result = True
  for i in range(1, N):
    if arr[i - 1] == arr[i][:len(arr[i - 1])]:
      result = False
      break
  
  print('YES') if result else print('NO')
