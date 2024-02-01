# 14502번: 연구소
from itertools import combinations
import copy, sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split()) # 가로, 세로 길이
virus = [] # 바이러스의 좌표를 저장하고 있는 리스트
empty = [] # 빈 칸의 좌표를 저장하고 있는 리스트(벽을 세울 수 있는 후보들을 저장하고 있는 리스트)
graph = []
for r in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for c in range(m):
        if graph[r][c] == 2:
            virus.append((r, c))
        elif graph[r][c] == 0:
            empty.append((r, c))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)] # 방문여부를 저장하는 리스트

def dfs(x, y, graph, visited):
    visited[x][y] = True
    graph[x][y] = 300 # 바이러스가 퍼져버린 칸은 300임


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 칸을 초과하는 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 벽으로 간 경우
        if graph[nx][ny] == 1:
            continue
        # 다른 바이러스의 칸으로 간 경우
        # if graph[nx][ny] == 2:
        #     continue
        if not visited[nx][ny]:
            if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                dfs(nx, ny, graph, visited)


# 안전 영역의 개수를 리턴해주는 함수
def check_safe_place(graph):
    n = len(graph)
    m = len(graph[0])
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                answer += 1

    return answer




wall_candidate = list(combinations(empty, 3)) # 벽을 설치할 수 있는 좌표 3개씩을 저장한 리스트

temp_graph = copy.deepcopy(graph)
temp_visited = copy.deepcopy(visited)

answer = 0

for candidate in wall_candidate:
    for w_x, w_y in candidate:
        temp_graph[w_x][w_y] = 1
    for v in virus:
        x, y = v
        dfs(x, y, temp_graph, temp_visited)
    answer = max(answer, check_safe_place(temp_graph))
    temp_graph = copy.deepcopy(graph)
    temp_visited = copy.deepcopy(visited)


print(answer)


    




    
