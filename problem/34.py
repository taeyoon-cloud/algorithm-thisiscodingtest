# 18353번: 병사 배치하기
n = int(input()) # 병사의 수
arr = list(map(int, input().split())) # 전투력
arr.reverse()

dp = [1] * n # dp 테이블

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외시켜야 하는 병사의 최소 수 출력
print(n - max(dp))