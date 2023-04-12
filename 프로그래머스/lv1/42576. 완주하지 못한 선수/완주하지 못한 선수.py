def solution(participant, completion):
    # 출력: 완주하지 못한 선수의 이름
    
    # 조건:
    # 동명이인 존재 가능 -> 이 말은 최대 두명 까지만 이름이 같다는 말인가?
    # 1 <= 참여 선수 수 <= 100000
    # len(completion) == len(participant) - 1
    # 1 <= len(참가자이름) <= 20
    
    # participant를 ['이름', index]로 해시 테이블에 저장한다 치면
    # address는 hash('이름')을 사용?
    # 그럼 얼만큼의 사이즈로 테이블을 만들어야 할까
    # 이름이 달라도 address가 겹치면 어떻게 제어?
    
    # 그냥 dict 쓰면 '이름', 1 을 기본으로 저장하고 존재하면 value를 높이면 되지 않나
    # case 1. completion -> dict 저장 후
    # participant으로 돌면서 존재하지 않으면 그 선수 리턴
    # 존재하면 해당 선수의 value -1
    # 반복
    # 일단 이렇게 시도 ㄱ
    
    dict = {}
    for i, x in enumerate(completion):
        if dict.get(x) is None:
            dict[x] = 1
        else:
            dict[x] = dict.get(x) + 1
    
    for x in participant:
        if dict.get(x) is None:
            return x
        else:
            if dict.get(x) == 1:
                del dict[x]
            else:
                dict[x] -= 1