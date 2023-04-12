def solution(nums):
    # 출력: 가장 많은 종류의 폰켓몬을 선택한 개수
    
    # 체크할 조건
    # 1 <= N <= 10000
    # 1 <= 종류 번호 <= 200000
    # 선택 방법이 여러가지여도 최댓값 하나만 리턴
    
    # 해시를 사용?
    # 그냥 중복 제거 후
    # 개수가 N/2 이상이면 return N/2
    # 이하면 return 개수
    # 이러면 되지 않을까
    
    after_set_len = len(list(set(nums)))
    select_limit = len(nums) / 2
    if after_set_len > select_limit:
        return select_limit
    else:
        return after_set_len
