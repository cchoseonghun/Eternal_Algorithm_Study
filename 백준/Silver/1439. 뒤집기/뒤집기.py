S = input()
to_one, to_zero = 0, 0

if S[0] == '0':
  to_one += 1
else:
  to_zero += 1

for i in range(len(S) - 1):
  if S[i] != S[i + 1]:
    if S[i + 1] == '1':
      to_zero += 1
    else:
      to_one += 1

print(min(to_one, to_zero))