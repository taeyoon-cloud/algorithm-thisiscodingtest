# 간단한 다익스트라 코드 => O(V^2)
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드개수 n, 간선개수 m
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)


for _ in range(m):
    a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])