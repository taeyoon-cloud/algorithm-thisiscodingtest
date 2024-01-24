# 모험가 길드
# 틀린 풀이
# 5
# 1 2 3 4 5
# n = int(input())
# fears = list(map(int, input().split()))

# fears.sort() # 오름차순 정렬

# count = 0 # 그룹 수
# index = 0
# while True:
#     index += fears[index]
#     if index >= n:
#         break
#     count += 1
    
# print(count)




n = int(input())
fears = list(map(int, input().split()))

fears.sort()

count = 0 # 현재 그룹의 사람 수
result = 0 # 총 그룹 수

for fear in fears:
    count += 1 # 현재 그룹의 사람 수 증가
    if count >= fear: # 만약 현재 그룹의 사람 수가 현재 확인하고 있는 모험가의 공포도보다 크거나 같다면
        result += 1 # 바로 그룹 형성해버림(그룹 수의 최댓값을 구해야 하므로, 그룹의 사람 수는 최소가 되어야 한다.)
        count = 0 # 다시 현재 그룹 사람 수를 0으로 초기화하고 반복문 처음부터 실행

print(result)