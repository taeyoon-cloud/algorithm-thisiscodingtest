# 11404번: 플로이드
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수

graph = [[INF] * (n+1) for _ in range(n+1)] # 최단 거리를 저장하는 2차원 리스트

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    # 입력받은 거리가 원래 입력된 거리보다 작은 경우에만 거리 입력
    if graph[a][b] > c:
        graph[a][b] = c

# 플로이드워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
