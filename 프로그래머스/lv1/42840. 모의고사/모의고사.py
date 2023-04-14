def solution(answers):
    # 출력: 가장 많은 문제를 맞힌 사람 번호
    
    # 조건:
    # len(answers) <= 10000
    # 출력이 여럿일 경우 오름차순 정렬
    
    # 1번: 1, 2, 3, 4, 5 반복
    # 2번: 2, 1, 2, 3, 2, 5 반복
    # 3번: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 반복
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []
    
    for i, x in enumerate(answers):
        if x == p1[i % len(p1)]:
            score[0] += 1
        if x == p2[i % len(p2)]:
            score[1] += 1
        if x == p3[i % len(p3)]:
            score[2] += 1
            
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
        
    return result