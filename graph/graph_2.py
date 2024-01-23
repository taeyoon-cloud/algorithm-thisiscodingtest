def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N,M = map(int, input().split())
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

result = []

for i in range(M):
    command, a, b = map(int, input().split())

    if command == 0:
        union_parent(parent, a, b)
    elif command == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            result.append("YES")
        else:
            result.append("NO")


for res in result:
    print(res)
