def solution(food):
    # 음식의 종류: 배열의 인덱스
    # 배열의 인덱스 순서는 칼로리가 적은 순서
    # but, food[0]은 물이며 항상 1
    
    # 인덱스 번호에 대해 // 2(몫) = 개수 
    # 인덱스를 개수만큼 반복
    # 인덱스 끝까지 진행
    # 인덱스가 끝나면 0 입력 후 지금까지 작성한 문자열을 거꾸로 작성하면 끝?
    
    answer = ''
    
    # for x in range(1, len(food)):
    #     개수 = food[x] // 2
    #     print(str(x) * 개수)  # 1, 22, 333 출력
        
    # 위 코드를 토대로 물 앞부분의 문자열을 구하면
    앞부분 = [str(x) * (food[x] // 2) for x in range(1, len(food)) if (food[x] // 2) > 0]
    
    answer += ''.join(앞부분)
    앞부분.reverse()  # 뒷부분
    answer += '0'
    answer += ''.join(앞부분)
    
    return answer