def solution(array, commands):
    # 출력: k번째 수
    
    # commands = [i, j, k]로 된 배열
    # 
    # if commands = [2, 5, 3]
    # test = [1, 5, 2, 6, 3, 7, 4][2-1:5]
    # print(sorted(test)[3-1])
    # [i, j, k] = commands
    # print(i, j, k)
    
    return [sorted(array[i-1:j])[k-1] for [i, j, k] in commands]
