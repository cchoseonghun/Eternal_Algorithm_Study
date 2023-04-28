for _ in range(int(input())):
  N = int(input())

  def DFS(x, sum):
    if x == N:
      if eval(sum.replace(' ', '')) == 0:
        print(sum)
      return
    next = x+1
    DFS(next, sum+' '+str(next))
    DFS(next, sum+'+'+str(next))
    DFS(next, sum+'-'+str(next))
  DFS(1, '1')
  print()