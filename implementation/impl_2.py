location = input()

x = int(location[1])
y = ord(location[0]) - ord('a') + 1

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]


result = 0
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    
    else:
        result += 1


print(result)