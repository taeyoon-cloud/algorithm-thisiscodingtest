# 18405번: 경쟁적 전염
from collections import deque

n, k = map(int, input().split())
graph = []
queue = deque([]) # 바이러스의 좌표를 저장하기 위한 리스트
start_list = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(n):
        if graph[i][j] != 0:
            start_list.append((i, j, graph[i][j]))

start_list.sort(key=lambda x:x[2])
start_list = deque(start_list)


s, start_x, start_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]



# 바이러스 a가 x,y에서 1초 동안 퍼지게 하는 함수
def bfs(x, y, a, temp_queue):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        # 0이 아니라면 그 칸에는 이미 다른 바이러스가 들어간 것
        if graph[nx][ny] != 0:
            continue
        
        # 0이라면 바이러스가 아직 전염되지 않았으므로 바이러스 i 전염
        if graph[nx][ny] == 0:
            graph[nx][ny] = a
            temp_queue.append((nx, ny, a))

   

# 여러 큐들을 가지고 있는 큐
# 각 큐는 각 초마다 출발해야할 바이러스에 대한 정보를 가지고 있다.
real_queue = deque([start_list])
 
while s > 0:
    queue = real_queue.popleft()
    temp_queue = deque([]) # 각 초마다 감염될 큐에 대한 정보를 가지고 있는 큐
    while queue:
        now = queue.popleft()
        x, y, virus_num = now
        bfs(x, y, virus_num, temp_queue)
    real_queue.append(temp_queue)
    s -= 1
       

print(graph[start_x-1][start_y-1])
            