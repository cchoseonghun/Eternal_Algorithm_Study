coins = [500, 100, 50, 10, 5, 1]
target = 1000 - int(input())

result = 0
for coin in coins:
  n = target // coin
  target -= coin * n
  result += n

print(result)