def solution(t, p):
    # t를 p와 같은 길이인 문자열로 자른 배열 반환
    # 배열을 돌며 p와 비교해 작거나 같은 수로 배열 반환
    # 마지막에 구한 배열 길이 반환
    
    target_arr = []
    start = 0
    end = len(p)
    while end <= len(t):
        target = t[start:end]
        start += 1
        end += 1
        target_arr.append(int(target))
    return sum([1 for x in target_arr if x <= int(p)])