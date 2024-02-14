# 1932번: 정수 삼각형
n = int(input()) # 삼각형의 크기

graph = [] # 삼각형을 이루고 있는 수를 저장하는 리스트

for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)


# dp 테이블
dp = [[0] * n for _ in range(n)]


# 점화식을 통해 dp 테이블 갱신
for i in range(n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + graph[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + graph[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + graph[i][j]


# 최댓값 출력
print(max(dp[n-1]))