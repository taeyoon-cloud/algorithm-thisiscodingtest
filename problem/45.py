# 3665번: 최종 순위
from collections import deque
import sys

input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수
while t:
    n = int(input()) # 팀의 수 n
    rank = list(map(int, input().split())) # 팀의 순위를 저장하는 리스트
    graph = [[False] * (n+1) for _ in range(n+1)] # 본인보다 낮은 순위들을 가리키는 리스트
    indegree = [0] * (n+1) # 진입차수를 저장하는 리스트


    for i in range(n):
        temp = rank[i+1:] # rank[i]보다 낮은 순위들 -> 가리켜야 함
        for num in temp:
            graph[rank[i]][num] = True
            indegree[num] += 1 # 진입차수 증가




    m = int(input()) # 상재거 등수가 바뀐 쌍의 수

    # 간선 방향 뒤집기
    for _ in range(m):
        a, b = map(int, input().split())

        if graph[a][b]:
            graph[a][b] = False
            indegree[b] -= 1
            graph[b][a] = True
            indegree[a] += 1
        else:
            graph[a][b] = True
            indegree[b] += 1
            graph[b][a] = False
            indegree[a] -= 1



    # 위상 정렬 시작
    queue = deque([]) # indegree가 0인 순위를 넣을 큐
    answer = [] # 올해 순위 리스트를 담을 리스트


    # 시작 노드(진입차수가 0인 노드) 큐에 넣기
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)


    # 만약 순위가 다 정해지기 전에 큐가 빈다면, cycle이 발생한 것 -> IMPOSSIBLE 출력
    # 만약 각 반복문마다 진입차수가 0인 노드가 2개 이상이라면 -> 순위가 확정되지 않은 것 -> ? 출력
    cycle = False
    certain = True
    for _ in range(n):
        # 사이클 발생
        if len(queue) == 0:
            cycle = True
            break
        
        # 확정 안됨
        elif len(queue) >= 2:
            certain = False
            break

        now = queue.popleft()
        answer.append(now)

        for i in range(1, n+1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)



    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for num in answer:
            print(num, end=' ')
        print()

    t -= 1