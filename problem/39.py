# 화성 탐사
import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

# 최단 거리 탐색
def dijkstra():
    q = []
    
    n = int(input()) # 맵 크기
    graph = [list(map(int, input().split())) for _ in range(n)] # 에너지 소모량 입력
    distance = [[INF] * n for _ in range(n)] # 최단 거리를 저장하는 2차원 리스트

    distance[0][0] = graph[0][0] # 출발칸 거리 초기화
    heapq.heappush(q, (distance[0][0], (0, 0))) # 시작점 큐에 넣기

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 큐가 빌 때까지
    while q:
        dist, now = heapq.heappop(q)
        now_x, now_y = now

        # 이미 처리된 적 있는 노드라면 무시
        if distance[now_x][now_y] < dist:
            continue
        
        # 현재 노드와 인접한 4개의 노드를 확인
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            # 지도를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            cost = dist + graph[nx][ny]
            # 만약 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, (nx, ny)))

    print(distance[n-1][n-1])


t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    dijkstra()



            










