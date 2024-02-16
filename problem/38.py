# # 정확한 순위
# 다익스트라 풀이
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # n은 학생 수, m은 두 학생의 성적을 비교한 횟수
graph = [[] for _ in range(n+1)]
connected = [[False] * (n+1) for _ in range(n+1)] # connected[i][j] = i->j로 연결되어 있는지 여부를 저장

# 성적 비교 입력
for _ in range(m):
    a, b = map(int, input().split()) # a번 학생이 b번 학생보다 성적이 낮다.
    graph[a].append(b)


# start보다 큰 수의 경우 connected[start][i] = True로 바꾸는 함수
def dijkstra(start):
    q = []
    heapq.heappush(q, start)
    while q:
        now = heapq.heappop(q)


        for i in graph[now]:
            if not connected[start][i]:
                connected[start][i] = True
                heapq.heappush(q, i)


# num이 순위를 확인할 수 있는 숫자인지 확인하는 함수
def check_rank(num):
    row = connected[num][1:]
    more_than_num = row.count(True)

    less_than_num = 0
    for i in range(1, n+1):
        if connected[i][num]:
            less_than_num += 1
    
    if more_than_num + less_than_num == n - 1:
        return True
    else:
        return False


# 1~n번까지의 학생과 연결된 학생들을 찾는다.
for i in range(1, n+1):
    dijkstra(i)

# i가 순위를 확인할 수 있는 숫자인지 확인하는 함수
answer = 0
for i in range(1, n+1):
    if check_rank(i):
        print(i)
        answer += 1

print(answer)

# 플로이드-워셜 풀이
# INF = int(1e9)

# n, m = map(int, input().split())
# graph = [[INF] * (n+1) for _ in range(n+1)]

# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b:
#             graph[a][b] = 0


# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1


# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

# for g in graph:
#     print(g)


# result = 0
# # 각 학생을 번호에 따라 한 명씩 확인하여 도달 가능한지 체크
# for i in range(1, n+1):
#     count = 0
#     for j in range(1, n+1):
#         if graph[i][j] != INF or graph[j][i] != INF:
#             count += 1
#     if count == n:
#         result += 1

# print(result)