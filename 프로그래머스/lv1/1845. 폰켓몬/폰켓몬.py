def solution(nums):
    unique = list(set(nums))
    L = len(unique)
    M = len(nums) / 2
    if L < M:
        return L
    else:
        return M
        