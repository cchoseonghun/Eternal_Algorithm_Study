def solution(k, m, score):
    # [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
    # [ 1,, 2]
    # k=4, m=3 일 때
    # 4, 4, 4 = 12
    # 4, 4, 4 = 12
    # 1, 1, 2 = 3
    # 2, 2, 2 = 6
    
    answer = 0
    temp = 0
    # score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
    # score.count(k) # 4 포함 개수 = 6
    # score.count(k) // m # 나올 수 있는 상자 개수
    # 상자 안의 최저 점수 사과 * 사과 개수 * 상자 개수
    # 현재 점수 k * 사과 개수 m * 상자 개수
    # 대신 이전 점수에서 남은 사과 저장해놨다 모자른 만큼 써야 함
    
    # answer += k * m * ((score.count(k) + temp) // m)
    # temp = (score.count(k) + temp) % m  # 상자에 못담은 사과 개수
    # k -= 1
    # 이걸 k가 0 이상일 경우 계속 반복
    
    while k > 0:
        answer += k * m * ((score.count(k) + temp) // m)
        temp = (score.count(k) + temp) % m
        k -= 1
    
    return answer