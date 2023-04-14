def solution(sizes):
    # 출력: 가장 작은 지갑의 크기

    # 가로, 세로에 대해 더 큰걸 가로에 몰아넣고
    # 제일 큰 가로, 세로 만큼의 지갑을 만들기
    
    max_w, max_h = 0, 0
    for one in sizes:
        if one[0] > one[1]:
            max_w = max(max_w, one[0])
            max_h = max(max_h, one[1])
        else:
            max_w = max(max_w, one[1])
            max_h = max(max_h, one[0])
    return max_w * max_h