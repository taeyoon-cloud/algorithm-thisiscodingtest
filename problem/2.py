# 곱하기 혹은 더하기
numbers = list(map(int, input()))

# 0, 1의 경우에는 더하고, 나머지는 곱한다.

total = numbers[0] # 만들어질 수 있는 가장 큰 수

for i in range(1, len(numbers)):
    if numbers[i] <= 1: # 확인하는 수가 0또는 1이라면
        total += numbers[i] # 더하기
    elif total == 0: # 만약 처음 수가 0이라면
        total += numbers[i] # 더하기
    else: 
        total *= numbers[i] # 그 외의 수는 다 곱하기



print(total)