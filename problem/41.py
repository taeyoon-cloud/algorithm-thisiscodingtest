# 여행 계획
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split()) # n은 여행지의 수, m은 여행 계획에 속한 도시의 수
connect = set() # 연결된 도시 (a, b) 튜플을 저장하는 집합
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            if i > j:
                connect.add((j+1, i+1))
            else:
                connect.add((i+1, j+1))

plan = list(map(int, input().split())) # 여행 계획에 대한 정보를 담는 리스트
parent = [i for i in range(n+1)]


# 연결된 도로는 union 연산 수행
for a, b in connect:
    union_parent(parent, a, b)

# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인(여행 계획에 속하는 모든 노드가 서로 연결되어 있는지 확인)
answer = "YES"
for i in range(m-1):
    start = plan[i]
    end = plan[i+1]

    if parent[start] == parent[end]:
        continue
    else:
        answer = "NO"
        break

print(answer)