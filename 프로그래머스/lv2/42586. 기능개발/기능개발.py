def solution(progresses, speeds):
    # 출력: 각 배포마다 배포되는 기능의 수로 된 배열 리턴
    
    # 조건
    # 2번째가 먼저 100을 채워도
    # 1번째가 100이 되야 같이 배포 가능
    
    # speeds의 원소는 1이상 100 이하
    # progresses 원소는 1이상 100 미만
    # len(progresses) <= 100
    
    # 한번 for문 돌 때 마다 pregresses의 각 원소에
    # speeds의 원소를 인덱스에 맞게 더하고
    # 0번째 인덱스의 값이 100이 넘을 경우 이어서 100이 넘는 기능들 모두 배포
    # 즉, 큐에서 dequeue하듯 빼면 될듯
    
    # 의문: 100 100 95 100 인 경우 배포 후에 95 100이 남는지 95만 남는지?
    # 95, 90, 99, 99, 80, 99
    # 96, 91, 100, 100, 81, 100
    # 97, 92, 100, 100, 82, 100
    # 98, 93, 100, 100, 83, 100
    # 99, 94, 100, 100, 84, 100
    # 100, 95, 100, 100, 85, 100
    # -> 95 100이 남는 방식
    
    answer = []
    while len(progresses) > 0:
        progresses = [x + y for x, y in zip(progresses, speeds)]
        done = 0
        while len(progresses) != 0 and progresses[0] >= 100:
            del progresses[0]
            del speeds[0]
            done += 1
        if done > 0:
            answer.append(done)
        
    return answer