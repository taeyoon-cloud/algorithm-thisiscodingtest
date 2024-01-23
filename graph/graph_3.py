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


n,m = map(int, input().split())
graph = []
parent = [0] * (n+1)
result = [] # 출력값

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

for i in range(1, n+1):
    parent[i] = i

# cost가 적은 edge순으로 정렬
graph.sort()

for edge in graph:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b): # 사이클을 형성하지 않을 경우
        union_parent(parent, a, b)
        result.append(cost)

print(sum(result[:-1]))


