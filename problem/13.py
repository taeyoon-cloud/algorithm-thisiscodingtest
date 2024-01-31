# 15686번: 치킨 배달
from itertools import combinations

n, m = map(int, input().split())
graph = []
INF = 987654321

# 0: 빈 칸 / 1: 집 / 2: 치킨집
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


# 임의의 두 칸 사이의 거리를 구하는 함수
def calculate_distance(house, chicken_house):
    r1, c1 = house
    r2, c2 = chicken_house
    return abs(r1-r2) + abs(c1-c2)

houses = [] # 집의 좌표를 저장하는 리스트
chicken_houses = [] # 치킨 집의 좌표를 저장하는 리스트

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chicken_houses.append((i, j))


# 치킨 집 중 1~m개를 선택한 경우의 수들을 저장하고 있는 리스트들을 저장한 리스트
chicken_candidates = []
for i in range(m, m+1):
    temp = list(combinations(chicken_houses, i))
    chicken_candidates.append(temp)

# print(chicken_candidates)

for candidates in chicken_candidates: # 1~m개를 선택한 경우의 수를 저장하는 리스트
    real_total= INF # 최소 치킨 거리를 저장하기 위한 변수
    for chicken_houses in candidates:
        sum_min_distance = 0 # 뽑은 치킨 집들에 대한 치킨 거리를 저장하는 변수
        for house in houses:
            min_distance = INF # 각 집에서 치킨 집까지의 최소 거리를 저장하는 변수
            for chicken_house in chicken_houses:
                min_distance = min(min_distance, calculate_distance(house, chicken_house))
            sum_min_distance += min_distance
        real_total = min(real_total, sum_min_distance)


print(real_total)