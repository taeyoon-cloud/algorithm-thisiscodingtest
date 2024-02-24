# 2887번: 행성 터널
import sys

input = sys.stdin.readline

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


n = int(input()) # 행성 수
parent = [i for i in range(n)] # 특정 노드의 루트 노드를 저장하는 리스트

INF = int(1e9)
# 행성의 3차원 좌표를 x, y, z 각각 저장하는 리스트
x_coord = []
y_coord = []
z_coord = []

for i in range(n):
    x, y, z = map(int, input().split())
    x_coord.append((x, i))
    y_coord.append((y, i))
    z_coord.append((z, i))

x_coord.sort()
y_coord.sort()
z_coord.sort()

# (거리, 도시a, 도시a와 연결된 도시b) 튜플을 저장하는 리스트들
edges = []

for i in range(n-1):
    edges.append((x_coord[i+1][0] - x_coord[i][0], x_coord[i][1], x_coord[i+1][1]))
    edges.append((y_coord[i+1][0] - y_coord[i][0], y_coord[i][1], y_coord[i+1][1]))
    edges.append((z_coord[i+1][0] - z_coord[i][0], z_coord[i][1], z_coord[i+1][1]))

edges.sort() # 거리를 기준으로 오름차순 정렬

answer = 0 # 모든 행성을 터널로 연결하는데 필요한 최소 비용
for edge in edges:
    dist, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += dist

print(answer)