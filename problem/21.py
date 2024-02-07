# 16234번: 인구 이동
from collections import deque
import copy

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [[False] * n for _ in range(n)]

# graph[i][j]에서 인구 이동할 수 있는 국가들을 BFS로 탐색
def bfs(i, j):
    queue = deque([(i, j)])
    country = [(i, j, graph[i][j])] # graph[i][j]에서 인구 이동할 수 있는 국가를 담은 리스트
    visited[i][j] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                temp = abs(graph[x][y] - graph[nx][ny])
                if not visited[nx][ny] and temp >= l and temp <= r:
                    queue.append((nx, ny))
                    country.append((nx, ny, graph[nx][ny]))
                    visited[nx][ny] = True

    return country


index = 0 # 인구이동을 한 날짜 수

while True:
    answer = True # 인구 이동이 일어났다면 True
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                temp_total = 0
                country = bfs(i, j)

                # country 리스트의 길이가 1보다 크다면 인구이동이 일어날 것.
                if len(country) > 1:
                    answer = False

                # 인구 이동 과정
                for c in country:
                    temp_total += c[2]
                population = temp_total // len(country)
                for c in country:
                    graph[c[0]][c[1]] = population


    # 인구 이동이 안 일어난 경우, 정답을 출력하고 반복문 종료
    if answer:
        print(index)
        break

    # 방문 여부 초기화
    visited = [[False] * n for _ in range(n)]
    # 하루 경과
    index += 1