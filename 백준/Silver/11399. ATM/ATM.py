N = int(input())
P = list(map(int, input().split()))

P.sort()
total = 0

for x in range(N):
    for y in range(x+1):
        total += P[y]
print(total)
