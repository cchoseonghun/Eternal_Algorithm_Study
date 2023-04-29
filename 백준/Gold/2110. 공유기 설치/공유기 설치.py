import sys

# 이분 탐색 함수 정의
def binary_search(arr, start, end, c):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 1  # 첫번째 공유기는 무조건 설치
        prev = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - prev >= mid:
                cnt += 1
                prev = arr[i]
        if cnt >= c:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

# 입력 받기
n, c = map(int, input().split())
houses = [int(sys.stdin.readline()) for _ in range(n)]

# 이분 탐색 실행
houses.sort()
print(binary_search(houses, 1, houses[-1] - houses[0], c))
