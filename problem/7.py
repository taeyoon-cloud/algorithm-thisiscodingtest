# 럭키 스트레이트
n = input()

length = len(n)

left = n[:length // 2]
right = n[length//2:]

left_sum = sum(map(int, left))
right_sum = sum(map(int, right))

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
