def solution(clothes):
    result = 1
    D = {}
    for _, kind in clothes:
        D[kind] = 0
    for _, kind in clothes:
        D[kind] += 1
    for x in D.values():
        result *= x + 1
    return result - 1