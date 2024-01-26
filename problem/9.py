# 문자열 압축
def solution(s):
    min_length = 1001 # 압축했을 때, 가장 짧은 길이
    
    # s의 길이가 1이면 1 리턴
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s) // 2 + 1):
        j = 0
        temp_answer = '' # i개 단위로 잘라서 압축했을 때의 문자
        while j + i < len(s):
            temp = s[j:j+i] # 확인할 반복되는 문자
            count = 0 # 확인할 반복되는 문자가 반복되는 횟수
            while temp == s[j:j+i]:
                count += 1
                j += len(temp)
            if count == 1: # 반복 횟수가 1번인 경우에는 문자만 더함
                temp_answer += temp
            elif count > 1: # 반복 횟수가 2번 이상인 경우는 개수 + 문자를 더함
                temp_answer += (str(count) + temp)
                
            # print(temp_answer)
            
        temp_answer += s[j:] # 뒤에 남은 문자를 더해줌
        min_length = min(min_length, len(temp_answer)) # 문자열 길이가 짧은 것으로 업데이트
        
    return min_length
        
            
                
            