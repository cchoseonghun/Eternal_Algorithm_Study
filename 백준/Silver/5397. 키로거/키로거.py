for _ in range(int(input())):
  first, second = [], []

  for str in input():
    if str == '<':
      if first:
        second.append(first.pop())
    elif str == '>':
      if second:
        first.append(second.pop())
    elif str == '-':
      if first:
        first.pop()
    else:
      first.append(str)
  first.extend(reversed(second))
  print(''.join(first))