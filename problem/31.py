# 금광
t = int(input()) # 테스트 케이스 개수

def gold():
    n, m = map(int, input().split())
    graph = []
    data = list(map(int, input().split()))

    for i in range(n):
        graph.append(data[m*i:m*(i+1)])
    
    dp = [[0] * m for _ in range(n)] # dp 테이블

    # 초기값 지정
    for i in range(n):
        dp[i][0] = graph[i][0]


    # dp 테이블 갱신
    for j in range(m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1]) + graph[i][j]
            elif i == n - 1:
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1]) + graph[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + graph[i][j]
        
    # 채굴자가 얻을 수 있는 금의 최대 크기를 출력
    answer = 0
    for i in range(n):
        if answer < dp[i][m-1]:
            answer = dp[i][m-1]

    print(answer)


for _ in range(t):
    gold()