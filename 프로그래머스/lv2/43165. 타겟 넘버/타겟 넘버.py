from collections import deque

def solution(numbers, target):
    answer = 0
    stack = deque([(0, 0)])
    while stack:
        sum, index = stack.pop()
        if index == len(numbers):
            if sum == target:
                answer += 1
        else:
            stack.append((sum + numbers[index], index + 1))
            stack.append((sum - numbers[index], index + 1))
    return answer
