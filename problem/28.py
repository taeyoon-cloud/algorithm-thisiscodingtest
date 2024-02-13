# 고정점 찾기
def find_fix_point(array, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2 # 확인할 인덱스

    if array[mid] == mid:
        return mid

    # 배열의 값이 0보다 작은 경우에는 그 왼쪽 값들은 볼 필요 없다.
    # 오른쪽 확인
    if array[mid] < 0:
        return find_fix_point(array, mid + 1, end)
    
    # 확인할 인덱스의 값이 그 인덱스보다 작은 경우 왼쪽 값들을 볼 필요 없다.
    # 오른쪽 확인
    elif array[mid] < mid:
        return find_fix_point(array, mid + 1, end)
    
    # 확인할 인덱스의 값이 그 인덱스보다 큰 경우 오른쪽 값들을 볼 필요 없다.
    # 왼쪽 확인
    else:
        return find_fix_point(array, start, mid - 1)
    

n = int(input())
arr = list(map(int, input().split()))

answer = find_fix_point(arr, 0, n-1)

if answer == None:
    print(-1)
else:
    print(answer)
        
