N = int(input())
arr = []

for _ in range(N):
  arr.append(int(input()))

def select_sort(arr):
  for i in range(len(arr)):  # i -> 0, 1, 2, 3, 4
    min_index = i
    for j in range(i, len(arr)):
      if arr[min_index] > arr[j]:
        min_index = j
    print(arr[min_index])
    arr[i], arr[min_index] = arr[min_index], arr[i]

select_sort(arr)