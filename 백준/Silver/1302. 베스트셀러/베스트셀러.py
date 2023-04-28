books = {}
N = int(input())
for _ in range(N):
  name = input()
  if name in books:
    books[name] += 1
  else:
    books[name] = 1

arr = [[] for _ in range(N+1)]
for 책이름, 개수 in books.items():
  arr[개수].append(책이름)

for i in range(len(arr)-1, -1, -1):
  if len(arr[i]) > 0:
    arr[i].sort()
    print(arr[i][0])
    break