# 기둥과 보 설치
# 현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 기둥인 경우
            # 바닥 위 혹은 보의 한쪽 끝 부분 위 혹은 다른 기둥 위라면 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y -1, 0] in answer:
                continue
            return False # 아니라면 False 반환
        elif stuff == 1: # 설치된 것이 보인 경우
            # 한쪽 끝 부분이 기둥 위 혹은 양쪽 끝 부분이 다른 보와 동시에 연결이라면 정상
                if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                    continue
                return False # 아니라면 False 반환
    return True
            
            
    

def solution(n, build_frame):
    result = []
    
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0: # 삭제 하는 경우
            result.remove([x,y,stuff]) # 일단 삭제를 해본 뒤
            if not possible(result): # 가능한 구조물인지 확인
                result.append([x, y, stuff]) # 가능한 구조물이면 다시 설치
        if operate == 1: # 설치하는 경우
            result.append([x, y, stuff]) # 일단 설치를 해본 뒤
            if not possible(result): # 가능한 구조물인지 확인
                result.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 제거
                
    return sorted(result)
                
    
    return result