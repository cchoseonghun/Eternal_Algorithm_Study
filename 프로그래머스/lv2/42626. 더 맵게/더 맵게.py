# def solution(scoville, K):
    # 출력: 섞어야 하는 최소 횟수
    
    # 2 <= len(scoville) <= 1000000
    # 0 <= K <= 1000000000
    # scoville의 원소는 각각 0 이상 1000000 이하
    # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우 -1 리턴
    
    # 제일 작은 값 + (두 번째로 작은 값 * 2)
    # 제일 작은 값이 K 이상이 될 때 까지 반복
    # 반복한 횟수 체크
    # Min Heap 사용?
    
    # 음식 종류가 두 개만 남았는데 합쳤을 때 K를 못 넘는 경우 -1 리턴
    
    # 일단 무식하게 Min Heap 만들어보자
    
#     heap = Heap()
#     for x in scoville:
#         heap.insert(x)
        
#     answer = 0
#     while heap.peek() < K:
#         first = heap.pop()
#         second = heap.pop()
#         fusion = first + (second * 2)
#         heap.insert(fusion)
#         answer += 1
    
#     return answer

# class Heap:
#     def __init__(self):
#         self.heap_arr = list()
#         self.heap_arr.append(None)

#     def peek(self):
#         return self.heap_arr[1]
        
#     def move_up(self, inserted_idx):
#         if inserted_idx <= 1:
#             return False
#         parent_idx = inserted_idx // 2
#         if self.heap_arr[parent_idx] > self.heap_arr[inserted_idx]:
#             return True
#         else:
#             return False
        
#     def insert(self, data):
#         self.heap_arr.append(data)
        
#         inserted_idx = len(self.heap_arr) - 1
#         while self.move_up(inserted_idx):
#             parent_idx = inserted_idx // 2
#             if self.heap_arr[parent_idx] > self.heap_arr[inserted_idx]:
#                 self.heap_arr[parent_idx], self.heap_arr[inserted_idx] = self.heap_arr[inserted_idx], self.heap_arr[parent_idx]
#                 parent_idx = inserted_idx
#         return True
    
#     def move_down(self, popped_idx):
#         left_child_idx = popped_idx * 2
#         right_child_idx = popped_idx * 2 + 1
        
#         if left_child_idx >= len(self.heap_arr):  # 왼쪽이 없으면 오른쪽도 없음
#             return False
#         elif right_child_idx >= len(self.heap_arr):  # 오른쪽만 없음
#             if self.heap_arr[left_child_idx] < self.heap_arr[popped_idx]:
#                 return True
#             else:
#                 return False
#         else:
#             if self.heap_arr[left_child_idx] > self.heap_arr[right_child_idx]:
#                 if self.heap_arr[popped_idx] > self.heap_arr[right_child_idx]:
#                     return True
#                 else:
#                     return False
#             else:
#                 if self.heap_arr[popped_idx] > self.heap_arr[left_child_idx]:
#                     return True
#                 else:
#                     return False
                
#     def pop(self):
#         return_data = self.heap_arr[1]
#         self.heap_arr[1] = self.heap_arr[-1]
#         del self.heap_arr[-1]
#         popped_idx = 1
        
#         while self.move_down(popped_idx):
#             left_child_idx = popped_idx * 2
#             right_child_idx = popped_idx * 2 + 1

#             if right_child_idx >= len(self.heap_arr):  # 오른쪽만 없음
#                 if self.heap_arr[left_child_idx] < self.heap_arr[popped_idx]:
#                     self.heap_arr[left_child_idx], self.heap_arr[popped_idx] = self.heap_arr[popped_idx], self.heap_arr[left_child_idx]
#                     popped_idx = left_child_idx
#             else:
#                 if self.heap_arr[left_child_idx] > self.heap_arr[right_child_idx]:
#                     if self.heap_arr[popped_idx] > self.heap_arr[right_child_idx]:
#                         self.heap_arr[right_child_idx], self.heap_arr[popped_idx] = self.heap_arr[popped_idx], self.heap_arr[right_child_idx]
#                         popped_idx = right_child_idx
#                 else:
#                     if self.heap_arr[popped_idx] > self.heap_arr[left_child_idx]:
#                         self.heap_arr[popped_idx], self.heap_arr[left_child_idx] = self.heap_arr[left_child_idx], self.heap_arr[popped_idx]
#                         popped_idx = left_child_idx
        
#         return return_data




# 힙 클래스를 만들어 사용하는 방법은 런타임 에러와 시간 초과, 그냥 실패 등 실패 덩어리
# 다른 방법을 사용한다면 뭐가 있을까?
# 그냥 정렬 시킨다음에 빼기?

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    answer = 0
    print('K: ', K)
    while scoville[0] < K:
        if len(scoville) == 2 and (scoville[0] + (scoville[1] * 2) < K):
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        fusion = first + (second * 2)
        heapq.heappush(scoville, fusion)
        answer += 1
    
    return answer
