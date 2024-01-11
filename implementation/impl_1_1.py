n = int(input())
commands = list(input().split())

x, y = 1, 1

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

command_type = ["L", "R", "U", "D"]

for command in commands:
    for i in range(len(command_type)):
        if command == command_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    x = nx
    y = ny

print(x, y)