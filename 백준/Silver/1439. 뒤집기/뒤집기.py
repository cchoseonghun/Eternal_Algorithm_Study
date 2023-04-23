S = input()

def turn_zero(S):
  count = 0
  for i in range(len(S)-1):
    if int(S[i]) - int(S[i+1]) == 1:
      count += 1
    if (int(S[-1]) == 1 and int(S[-2]) == 1) or (int(S[-1]) == 1 and int(S[-2]) == 0):
      count += 1
  return count

def turn_one(S):
  count = 0
  for i in range(len(S)-1):
    if int(S[i+1]) - int(S[i]) == 1:
      count += 1
    if (int(S[-1]) == 0 and int(S[-2]) == 0) or (int(S[-1]) == 0 and int(S[-2]) == 1):
      count += 1
  return count

print(min(turn_zero(S), turn_one(S)))