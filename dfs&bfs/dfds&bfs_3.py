n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

x = 0
y = 0
count = 0

def dfs(x, y):
    arr[x][y] = 1


    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >=0 and nx < n and ny >= 0 and ny < m:
            if arr[nx][ny] == 0:
                dfs(nx, ny)


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            dfs(i, j)
            count += 1

print(count)