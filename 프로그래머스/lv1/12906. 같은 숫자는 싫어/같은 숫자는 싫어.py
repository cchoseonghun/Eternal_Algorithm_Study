def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i, x in enumerate(arr):
        if i == 0:
            answer.append(x)
        if answer[-1] != x:
            answer.append(x)
    return answer