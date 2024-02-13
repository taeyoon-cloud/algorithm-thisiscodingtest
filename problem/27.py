# 정렬된 배열에서 특정 수의 개수 구하기
# import sys
# from bisect import bisect_left, bisect_right

# input = sys.stdin.readline

# n, x = map(int, input().split())
# arr = list(map(int, input().rstrip().split()))

# cnt = bisect_right(arr, x) - bisect_left(arr, x)

# if cnt == 0:
#     print(-1)
# else:
#     print(cnt)


# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메소드
def count_by_value(array, x):
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)

    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0 # 값이 x개인 원소의 개수는 0개 이므로 0 반환
    
    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n-1)

    return b - a + 1


# 처음 위치를 찾는 이진 탐색 메소드
def first(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우에는 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid+1, end)
    

# 마지막 위치를 찾는 이진 탐색 메소드
def last(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n - 1 or array[mid+1] > target) and array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
    else:
        return last(array, target, mid+1, end)
    
n, x = map(int, input().split())
array = list(map(int, input().split()))

cnt = count_by_value(array, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)