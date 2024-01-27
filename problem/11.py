# 3190번: 뱀
from collections import deque

n = int(input()) # 보드 크기
k = int(input()) # 사과 개수

# 0: 빈 칸, 1: 사과, 2: 벽
graph = [[0] * (n+1) for _ in range(n+1)]



for i in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1


l = int(input()) # 뱀의 방향 변환 횟수 L
commands = deque() # 뱀의 뱡향 변환 정보 (초, 방향)을 저장하는 저장하는 큐
for i in range(l):
    sec, command = input().split()
    commands.append((int(sec), command))

# 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque([(x, y)]) # queue에는 현재 지렁이가 차지 하고 있는 칸이 들어간다.
    time = 0 # 게임 시간
    i = 0 # 방향을 가리키는 변수
    sec, command = commands.popleft() # 처음 방향 전환 정보

    while True:
        # 방향 전환
        if time == sec:
            if command == "L":
                i -= 1
                i %= 4
            elif command == "D":
                i += 1
                i %= 4
            if len(commands) != 0:
                sec, command = commands.popleft()
        
        nx = x + dx[i]
        ny = y + dy[i]



        # 벽에 닿은 경우 종료
        if nx <= 0 or nx > n or ny <= 0 or ny > n:
            break

        # 자기 몸에 부딪힌 경우 종료
        if (nx, ny) in queue:
            break

        # 이동한 칸에 사과가 없는 경우, 꼬리가 위치한 칸을 비우고, 머리가 위치한 칸은 추가
        if graph[nx][ny] == 0:
            queue.popleft()
            queue.append((nx, ny))
            x = nx
            y = ny

        # 이동한 칸에 사과가 있는 경우, 그 칸에 있는 사과가 없어지고, 꼬리는 그대로, 머리가 위치한 칸은 추가
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            queue.append((nx, ny))
            x = nx
            y = ny


        time += 1 # 시간 추가

    return time


result = bfs(1, 1)

print(result + 1)