import sys
sys.setrecursionlimit(100000)

def DFS(L, curr, target, numbers):
    result = 0
    if L == len(numbers):
        if curr == target:
            result += 1
        return result
    result += DFS(L + 1, curr + numbers[L], target, numbers)
    result += DFS(L + 1, curr - numbers[L], target, numbers)
    return result

def solution(numbers, target):
    return DFS(0, 0, target, numbers)
    