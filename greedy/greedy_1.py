n = int(input())
count = 0 # 거슬러야 할 동전 개수의 합

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += (n // coin)
    n %= coin

print(count)

