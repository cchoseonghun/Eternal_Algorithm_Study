file = input()
target = input()

# result = 0
# while file.find(target) >= 0:
#   target_index = file.find(target)
#   file = file[:target_index]+file[target_index+len(target):]
#   result += 1
# print(result)

# aaabbb, ab인 경우 1이어야 하는데 3이 출력

result = 0
def find(file, target):
  global result
  if file.find(target) >= 0:
    result += 1
    find(file[file.find(target)+len(target):], target)
  return
find(file, target)
print(result)