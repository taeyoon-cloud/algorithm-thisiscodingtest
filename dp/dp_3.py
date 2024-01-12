# n = int(input())
# arr = list(map(int, input().split()))

# dp = [0] * n


# dp[0] = arr[0]
# dp[1] = arr[1]
# dp[2] = arr[0] + arr[2]

# for i in range(3, n):
#     dp[i] = max(dp[i-3], dp[i-2]) + arr[i]

# print(max(dp))

n = int(input())
arr = list(map(int, input().split()))


dp = [0] * n

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])

print(dp[n-1])