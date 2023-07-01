import sys
input = sys.stdin.readline

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def pre_order(node):
  print(node.data, end='')
  if node.left != None:
    pre_order(nodes[node.left])
  if node.right != None:
    pre_order(nodes[node.right])
  
def in_order(node):
  if node.left != None:
    in_order(nodes[node.left])
  print(node.data, end='')
  if node.right != None:
    in_order(nodes[node.right])

def post_order(node):
  if node.left != None:
    post_order(nodes[node.left])
  if node.right != None:
    post_order(nodes[node.right])
  print(node.data, end='')

N = int(input())
nodes = {}
for _ in range(N):
  data, left, right = input().split()
  node = Node(data)
  if left != '.':
    node.left = left
  if right != '.':
    node.right = right
  nodes[data] = node
  
pre_order(nodes['A'])
print()
in_order(nodes['A'])
print()
post_order(nodes['A'])