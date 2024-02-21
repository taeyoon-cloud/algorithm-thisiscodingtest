# 숨바꼭질
import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)] # (도착노드, 거리)를 저장하기 위한 리스트
distance = [INF] * (n+1) # 최단거리를 저장하기 위한 리스트

# 노드 연결
for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 연결 및 거리는 1
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 이미 처리된 적 있는 노드면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 인접한 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘 실행
dijkstra(1)

# (번호, 거리)로 저장된 distance 리스트
new_distance = list(zip(range(1, n+1), distance[1:]))

new_distance.sort(key = lambda x: (-x[1],x[0])) # 거리 내림차순 배열, 번호 오름차순 배열

max_node = new_distance[0][0] # 숨어야 하는 헛간 번호
max_distance = new_distance[0][1] # 그 헛간까지의 거리
max_count = len(list(filter(lambda x: x[1] == max_distance, new_distance))) # 그 헛간과 같은 거리를 갖는 헛간의 개수

print(max_node, max_distance, max_count)

# max_node = 0
# max_distance = 0
# result = []

# for i in range(1, n+1):
#     if max_distance < distance[i]:
#         max_distance = distance[i]
#         max_node = i
#         result = [max_node]
#     elif max_distance == distance[i]:
#         result.append(i)

# print(max_node, max_distance, len(result))