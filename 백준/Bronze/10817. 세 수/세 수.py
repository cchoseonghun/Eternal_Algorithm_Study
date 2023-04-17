# 출력: 두번째로 큰 정수

# 첫째줄로 입력받음 ex) 10 20 30
# 1 <= A, B, C <= 100

arr = list(map(int, input().split()))

# 0,1
# 1,2
# 0,1

for i in range(len(arr)-1):
  for j in range(len(arr)-1-i):
    if arr[j] > arr[j+1]:
      arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr[1])