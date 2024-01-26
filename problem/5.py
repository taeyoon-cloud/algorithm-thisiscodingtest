# 볼링공 고르기
# from itertools import combinations

# n, m = map(int, input().split())
# balls = list(map(int, input().split()))

# candidates = list(combinations(balls, 2))

# result = 0
# for cand in candidates:
#     if len(cand) == len(set(cand)):
#         result += 1

# print(result)

n, m = map(int, input().split())
balls = list(map(int, input().split()))

array = [0] * (m+1)

for ball in balls:
    array[ball] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)