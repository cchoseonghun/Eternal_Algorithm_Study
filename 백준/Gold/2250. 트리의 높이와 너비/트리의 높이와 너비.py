import sys
input = sys.stdin.readline

class Node:
  def __init__(self, data):
    self.parent = None
    self.data = data
    self.left = None
    self.right = None

def in_order(node, L):
  global count
  while len(result) <= L:
    result.append([])
  if node.left is not None:
    in_order(tree[node.left], L + 1)
  # print(node.data, end=' ')
  result[L].append(count)
  count += 1
  if node.right is not None:
    in_order(tree[node.right], L + 1)

N = int(input())
tree = [0] * (N + 1)
for i in range(1, N + 1):
  tree[i] = Node(i)

for _ in range(N):
  data, left, right = map(int, input().split())
  if left != -1:
    tree[data].left = left
    tree[left].parent = data
  if right != -1:
    tree[data].right = right
    tree[right].parent = data

root = 0
for i in range(1, N + 1):
  if tree[i].parent is None:
    root = i
    break

result = [[]]
count = 1
in_order(tree[root], 0)

L = 0
M = 0
for i in range(len(result)):
  x = result[i]
  diff = max(x) - min(x) + 1
  if M < diff:
    L = i + 1
    M = diff
print(L, M)
