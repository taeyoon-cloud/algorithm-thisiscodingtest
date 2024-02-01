# 18352번: 특정 거리의 도시 찾기
from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int ,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1) # 방문 여부를 저장하는 리스트(0이면 방문x, 나머지는 방문까지의 거리)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs():
    queue = deque([x]) # 시작점을 큐에 넣고 시작
    visited[x] = 1 # 시작 점을 방문 처리
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[now] + 1


bfs()

check = False
for i in range(1, n+1):
    # visited 배열에 저장된 수들은 시작점에서의 최단거리 + 1인 값임
    # 그러므로 k+1을 확인해야 함
    if visited[i] == k+1:
        print(i)
        check = True

if not check:
    print(-1)
            


        