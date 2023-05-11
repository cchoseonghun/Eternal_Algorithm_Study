import sys
input = sys.stdin.readline

class Node:
  def __init__(self, data, left, right):
    self.parent = -1
    self.data = data
    self.left = left
    self.right = right

def in_order(L, node):
  global x
  while len(arr) < L + 1:
    arr.append([])
  if node.left != -1:
    in_order(L + 1, tree[node.left])
  arr[L].append(x)
  x += 1
  if node.right != -1:
    in_order(L + 1, tree[node.right])

N = int(input())
tree = {}
for i in range(1, N + 1):
  tree[i] = Node(i, -1, -1)

for _ in range(N):
  data, left, right = map(int, input().split())
  tree[data].left = left
  tree[data].right = right
  if left != -1:
    tree[left].parent = data
  if right != -1:
    tree[right].parent = data

x = 1
L = 1
arr = [[]]
root = 1
for i in range(1, N + 1):
  if tree[i].parent == -1:
    root = i
in_order(L, tree[root])

max_i = 0
max_w = 0
for i in range(len(arr)):
  if len(arr[i]) > 0:
    new_w = max(arr[i]) - min(arr[i]) + 1
    if max_w < new_w:
      max_i = i
      max_w = new_w

print(max_i, max_w)