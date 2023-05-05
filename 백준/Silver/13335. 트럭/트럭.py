n, w, L = map(int, input().split())
waiting = list(map(int, input().split()))
proceeding = [0] * w
counting = 0

while len(waiting) != 0 or sum(proceeding) != 0:
  counting += 1
  target = proceeding.pop(0)
  proceeding.append(0)
  if len(waiting) > 0:
    if sum(proceeding) + waiting[0] <= L:
      proceeding[-1] = waiting.pop(0)

print(counting)
