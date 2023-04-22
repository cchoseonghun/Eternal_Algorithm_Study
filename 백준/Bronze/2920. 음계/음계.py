arr = ['None', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C']

str = ''
for i in list(map(int, input().split())):
  str += arr[i]
if str == 'cdefgabC':
  print('ascending')
elif str == 'Cbagfedc':
  print('descending')
else:
  print('mixed')