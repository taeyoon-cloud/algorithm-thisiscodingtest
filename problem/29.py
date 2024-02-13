# 2110번: 공유기 설치
n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort() # 이진 탐색을 위해 오름차순 정렬

start = array[1] - array[0] # 공유기 사이 거리의 최솟값(첫번째 집에는 무조건 공유기를 설치한다.)
end = array[-1] - array[0] # 공유기 사이 거리의 최댓값
result = 0

while start <= end:
    mid = (start + end) // 2 # 가장 인접한 공유기 사이의 거리
    value = array[0]
    count = 1 # 공유기 설치 개수

    for i in range(1, n): # 앞에서 부터 설치
        if array[i] >= value + mid:
            value = array[i] # 공유기 설치 위치 변경
            count +=1 # 공유기 설치

    if count >= c: # 만약 C개 이상의 공유기를 설치할 수 있는 경우, 가장 인접한 공유기 사이의 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # 만약 C개 이상의 공유기를 설치할 수 없는 경우, 가장 인접한 공유기 사이의 거리를 감소
        end = mid - 1


print(result)
    
