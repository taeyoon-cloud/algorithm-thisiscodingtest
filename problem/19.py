# # 14888번: 연산자 끼워넣기
# from itertools import permutations
# INF = 1e10

# n = int(input()) # 숫자 개수
# arr = list(map(int, input().split())) # 숫자
# plus, minus, multiply, divide = map(int, input().split())

# oper = []
# for _ in range(plus):
#     oper.append("+")
# for _ in range(minus):
#     oper.append("-")
# for _ in range(multiply):
#     oper.append("*")
# for _ in range(divide):
#     oper.append("/")

# # 숫자 리스트와 연산자 리스트가 주어졌을 때, 값을 계산해서 리턴해주는 함수
# def calculate(arr, oper):
#     result = arr[0]
#     for i in range(n-1):
#         op = oper[i]
#         num = arr[i+1]

#         if op == "+":
#             result += num
#         elif op == "-":
#             result -= num
#         elif op == "*":
#             result *= num
#         elif op == "/":
#             if result < 0:
#                 temp = abs(result) // num
#                 result = -temp
#             else:
#                 result //= num
#     return result

# candidates = list(set(list(permutations(oper, n-1))))

# max_result = -INF
# min_result = INF

# for cand in candidates:
#     temp_result = calculate(arr, cand)
#     max_result = max(max_result, temp_result)
#     min_result = min(min_result, temp_result)

# print(max_result)
# print(min_result)
    

import sys
sys.setrecursionlimit(10**6)

n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최댓값과 최솟값 초기화
min_value = 1e10
max_value = -1e10

# DFS 메소드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        # 각 연산자에 대해 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)


