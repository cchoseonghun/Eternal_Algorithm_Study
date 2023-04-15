# 3
def decimal_check(N):
    if N <= 1:
        return False
    for x in range(2, N+1):
        if (N / x == N // x) and x != N:
            return False
    return True

answer = 0
def solution(numbers):
    # 출력: 만들 수 있는 소수의 개수
    
    # 순열 사용
    # numbers = "011"을
    # ['0', '1', '1']로 만들 방법?
    # 순열로 구한 값에 대한 소수 체크
    
    # 1. numbers -> 리스트로 가공
    # 2. 순열 함수
    # 3. 소수 확인 함수
    
    # 1
    n = [x for x in numbers]
    r = len(n)
    
    decimal_arr = []
    
    # 2
    checklist = [0] * r
    def DFS(L, target):
        global answer
        if L == target:
            x = int(''.join(result))
            if decimal_check(x) and x not in decimal_arr:
                decimal_arr.append(x)
                answer += 1
        else:
            for i in range(len(n)):
                if checklist[i] == 0:
                    result[L] = n[i]
                    checklist[i] = 1
                    DFS(L + 1, target)
                    checklist[i] = 0
    for x in range(1, len(n)+1):
        result = [0] * x
        DFS(0, x)
    
    return answer

