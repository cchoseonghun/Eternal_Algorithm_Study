n = int(input())
arr = [0] * 46

def recursion(n):
  if n <= 1:
    return n
  if arr[n] != 0:
    return arr[n]
  else:
    temp = recursion(n-1) + recursion(n-2)
    arr[n] = temp
    return temp

print(recursion(n))