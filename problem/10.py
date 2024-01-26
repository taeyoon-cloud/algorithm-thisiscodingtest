# 자물쇠와 열쇠
import copy

# key를 시계방향으로 회전시키는 함수
def rotate_right(arr):
    rotated_arr = [[0] * len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            rotated_arr[j][len(arr)-1-i] = arr[i][j]
            
    return rotated_arr


    
def solution(key, lock):
    n = len(lock)
    m = len(key)
    length = n + 2 * m - 2
    mapp = [[0] * length for _ in range(length)] 
    # 가로, 세로가 (n + 2*m - 2)인 전체 지도

    # map 가운데에 lock 위치
    for i in range(n):
        for j in range(n):
            mapp[m-1+i][m-1+j] = lock[i][j]
            
    # key 배치 시작
    check_mapp = copy.deepcopy(mapp) # 반복문을 돌면서 확인할 맵
    
    for i in range(len(mapp)-(m-1)):
        for j in range(len(mapp)-(m-1)):
            for _ in range(4):# 4번 회전
                key = rotate_right(key)
                
                # 자물쇠에 열쇠 넣기
                for k in range(m):
                    for l in range(m):
                        check_mapp[i+k][j+l] += key[k][l]
                    
                # 확인해야할 자물쇠
                check_lock = list(map(lambda x: x[m-1:m-1+n], check_mapp[m-1:m-1+n]))
                # print(check_lock)
                # 자물쇠의 모든 원소가 1이면 True 리턴
                if sum([row.count(1) for row in check_lock]) == n * n:
                    return True
                
                # 자물쇠의 모든 원소가 1이 아니라면, key를 다시 넣어서 확인해야 하므로 map 초기화
                check_mapp = copy.deepcopy(mapp)
    
    return False
            
    