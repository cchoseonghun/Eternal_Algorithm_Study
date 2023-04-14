def solution(triangle):
    # 거쳐간 숫자의 합
    
    # 1 <= len(triangle) <= 500
    # 각 원소는 0 이상 9999 이하
    
    # 시작은 세 꼭지점 중 하나
    # 꼭지점이 달라질 때가 문제
    
    # 세가지 경우의 대한 합을 구하고 서로 비교?
    # case 1. 그림에서 7이 시작인 경우
    # t[0][0] -> t[1][0] vs t[1][1]
    # F -> A vs B 라고 할 때
    # A, B의 x는 1씩 커지고 
    # A, B의 y는 F[x][y]에 대해 y, y+1
    
        # for x in range(len(triangle)):
        # c1 += triangle[x][F]
        # if triangle[x+1][F] 
    
    # case 2. 4가 시작인 경우
    # x는 1씩 작아짐
    # y는 ..
    
    # 근데 숫자가 같은 경우 문제 발생
    
    
    # 잠깐만, 각 인덱스 별로 현재 값을 유지하는게 아니라
    # 맨 마지막 인덱스 배열에 모든 합이 되게끔 쭈우욱 내려오면 되는거 아닌가?
    # 그래서 마지막 중 제일 높은 숫자 체크
    # 이 경우 두 부모중 큰 숫자로 해야하네..
    # 잠깐, 그럼 내가 처음에 생각한 각 꼭지점으로 돌려가며 구하는게 아닌가보네
    # 이럴 경우 마지막 4, 5, 2, 6, 5에서 두번째 5에 합 30이 들어가게 됨
    # 그럼 target인 자식의 노드가 이전 배열에서 자기 인덱스랑 자기 인덱스-1 노드를 비교해서 큰 수를 자기한테 더하면 되겠네?
    
    # 맨 위 꼭지점은 생략하고 for문을 1부터 len(tri) 까지
    for x in range(1, len(triangle)):
        # 해당 배열의 인덱스 0은 항상 그대로 이전 배열 0을 더한다.
        # 해당 배열의 마지막 인덱스는 항상 이전 배열의 마지막 요소 값을 더한다.
        for y in range(len(triangle[x])):
            if y == 0:
                triangle[x][0] += triangle[x-1][0]
            elif y == len(triangle[x])-1:
                triangle[x][-1] += triangle[x-1][-1] 
            else:
                if triangle[x-1][y] > triangle[x-1][y-1]:
                    triangle[x][y] += triangle[x-1][y]
                else:
                    triangle[x][y] += triangle[x-1][y-1]
                    
    return max(triangle[-1])