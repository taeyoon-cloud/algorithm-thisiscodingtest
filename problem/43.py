# 어두운 길

# 특정 노드가 속한 집합을 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 노드가 속한 집합을 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split()) # 집 개수 n, 도로 개수 m

parent = [i for i in range(n)] # 각 노드의 루트 노드를 저장하는 리스트
edges = [] # (비용, a, b) 튜플을 저장하는 리스트 -> 비용을 오름차순으로 정렬하기 편하도록 비용을 먼저 저장 / a, b는 연결된 두 노드

total = 0 # 전체 도로 비용의 합

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    total += cost

edges.sort() # 비용을 오름차순으로 정렬
result = 0 # 최소 신장 트리의 간선 비용의 합

for edge in edges:
    cost, a, b = edge

    # 사이클이 형성되지 않는 경우 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# 일부 가로등을 비활성하여 절약할 수 있는 최대 금액 = 전체 금액 - 최소로 구성되어야 하는 도로의 비용(최소 신장 트리를 구성한느 비용)
print(total - result)