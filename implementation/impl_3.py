n, m = map(int, input().split()) # 맵 크기
x, y, direction = map(int, input().split()) # 초기x, 초기y, 초기방향

# 맵 입력
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 방문한 칸 기록하기 위한 2차원 배열
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[x][y] = 1 # 처음 있던 칸은 방문한 칸


# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0 # count가 4가 되는 순간 제자리에서 한바퀴 돈것
result = 1 # 방문한 칸 수
while True:
    direction -= 1
    if direction == -1:
        direction = 3

    # 네 방향 모두 이미 가본 칸이거나 바다로 된 칸이라면 바라보는 방향을 유지한 상태로 뒤로간다. 뒤로 갈 수 없으면 이동 종료
    if count == 4:
        print("드가자")
        direction += 1
        nx = x - dx[direction]
        ny = y - dy[direction]
        if arr[nx][ny] == 1:
            print(nx, ny)
            print("갈수있는 칸이 없어!")
            break
        else:
            x = nx
            y = ny
            print(x, y)
            print("뒤로 한칸 이동했어")
            count = 0
            continue

    print(direction)

    nx = x + dx[direction]
    ny = y + dy[direction]

    # 바다인 경우 그 칸으로 갈 수 없다.
    if arr[nx][ny] == 1:
        count += 1
        print(nx, ny)
        print("바다야")
        continue
    elif visited[nx][ny] == 0:
        x = nx
        y = ny
        visited[nx][ny] = 1
        result += 1
        count = 0
        print(x, y)
        print("육지라서 이동했어")
    elif visited[nx][ny] == 1:
        count += 1
        print("이미 방문한 칸이야")
        continue


        


print(result)