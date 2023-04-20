def solution(numbers, target):
    # 출력: target이 되는 방법의 수
    
    # 조건: 
    # 2 <= len(numbers) <= 20
    # 1 <= numbers[i] <= 50
    # 1 <= target <= 1000
    
    # 구현: 
    # 0을 root로 잡고
    # DFS 방식으로 numbers의 각 원소마다 
    # 뺄지, 더할지를 선택해 합하면서 내려가며 
    # 마지막 depth에 도달했을 때 합이 target과 일치한다면 count +1
    
    # 1. 그래프 구현
    # 2. DFS 구현
    
    # sum을 같이 가져가야 하고
    # depth를 알기 위해 index도 가져가야 함
    
    # 재귀로 푸는 방법 밖에 일단 생각이 안나서 재귀로 도전
    global count
    count = 0
    
    def dfs(numbers, index, sum):
        global count
        if index == len(numbers):
            if sum == target:
                count += 1
            return
        dfs(numbers, index + 1, sum + numbers[index])
        dfs(numbers, index + 1, sum - numbers[index])
    
    dfs(numbers, 0, 0)
    return count