N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

if max(cranes) < max(boxes):
  print(-1)
  exit()

cranes.sort(reverse=True)
boxes.sort(reverse=True)

positions = [0] * N  # 각 index 번째 크레인이 바라보는 boxes index
checked = [False] * M  # boxes index의 박스가 옮겨졌는지 체크
count = 0  # 옮긴 box 수
result = 0  # 소요된 시간
while True:
  if count == M:
    break
  for i in range(N):
    while positions[i] < M:
      if boxes[positions[i]] <= cranes[i] and not checked[positions[i]]:
        checked[positions[i]] = True
        count += 1
        break
      positions[i] += 1
  result += 1
print(result)