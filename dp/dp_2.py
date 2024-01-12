INF = 987654321
n = int(input())

dp = [INF] * (n+1)

dp[1] = 0

for i in range(2, n+1):
    if i % 5 == 0:
        dp[i] = min(dp[i//5], dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3], dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2], dp[i])
    
    dp[i] = min(dp[i], dp[i-1]) + 1
    

print(dp)
