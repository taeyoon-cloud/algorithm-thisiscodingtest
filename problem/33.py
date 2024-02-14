# 14501번: 퇴사

# n = int(input())
# time = [0] # 상담하는데 필요한 기간
# price = [0] # 상담 이익

# dp = [0] * 21 # dp 테이블

# # 상담기간, 상담이익 추가
# for _ in range(n):
#     t, p = map(int, input().split())
#     time.append(t)
#     price.append(p)

# # dp 테이블 갱신
# for i in range(1, n+1):
#     dp[i+time[i]] = max(max(dp[:i+1])+price[i], dp[i+time[i]])

# # print(dp[1:])
# print(max(dp[:n+2]))



# 풀이 2.
n = int(input())
time = [] # 상담하는데 필요한 기간
price = [] # 상담 이익

dp = [0] * 21 # dp 테이블

# 상담기간, 상담이익 추가
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)
max_value = 0

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):
    t = time[i] + i
    # 상담이 기간 안에 끝나는 경우
    if t <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(price[i] + dp[t], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
