from heapq import heappush, heappop, heapify

def solution(scoville, K):
    # 출력: 섞은 횟수

    # 만들 수 없을 때 return -1
    # 섞 = 가장 맵 + (두번째 맵 * 2)
    answer = 0
    heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 2 and (scoville[0] + scoville[1] * 2 < K):
            return -1
        heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        answer += 1
    return answer