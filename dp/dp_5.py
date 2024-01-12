INF = 987654321

n, m = map(int, input().split())
coin_types = [int(input()) for _ in range(n)]

dp = [INF] * 10001
dp[0] = 0

for coin in coin_types:
    for j in range(coin, m+1):
        dp[j] = min(dp[j], dp[j-coin] + 1)


if dp[m] == INF:
    print(-1)
else:
    print(dp[m])