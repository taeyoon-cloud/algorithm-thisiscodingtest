# 18428번: 감시 피하기
import sys, copy
sys.setrecursionlimit(10**6)


# 장애물이 3개 설치된 해당 복도에서 
# 모든 학생들이 선생님의 감시를 피할 수 있는지 여부를 리턴하는 함수
def check():
    for t in teacher:
        teacher_x, teacher_y = t[0], t[1]
        # 상
        for i in range(teacher_x - 1, -1, -1):
            if graph[i][teacher_y] == 'O':
                break
            if graph[i][teacher_y] == 'S':
                return False
        # 하
        for i in range(teacher_x + 1, n):
            if graph[i][teacher_y] == 'O':
                break
            if graph[i][teacher_y] == 'S':
                return False
        # 좌
        for j in range(teacher_y - 1, -1, -1):
            if graph[teacher_x][j] == 'O':
                break
            if graph[teacher_x][j] == 'S':
                return False
        # 우
        for j in range(teacher_y + 1, n):
            if graph[teacher_x][j] == 'O':
                break
            if graph[teacher_x][j] == 'S':
                return False
    return True



# 장애물 설치 -> 백트래킹
def back_tracking(cnt):
    global answer
    if cnt == 3:
        if check():
            answer = True
            return
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    back_tracking(cnt + 1)
                    graph[i][j] = 'X'

            
n = int(input()) # 복도 크기
graph = [] # 복도
teacher = [] # 선생님의 좌표를 저장하는 리스트
answer = False # 이게 True면 Yes 출력, 아니면 No 출력

for i in range(n):
    row = list(input().split())
    graph.append(row)
    for j in range(n):
        if graph[i][j] == "T":
            teacher.append((i, j))


back_tracking(0)

if answer:
    print("YES")
else:
    print("NO")