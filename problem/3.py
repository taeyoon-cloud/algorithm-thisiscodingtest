# 문자열 뒤집기
n = list(map(int, input()))

# 1뒤집기
count_1 = 0
flag_1 = 0
for i in n:
    if i == 1 and flag_1 == 0:
        count_1 += 1
        flag_1 = 1
    if i == 0:
        flag_1 = 0


# 0뒤집기
count_0 = 0
flag_0 = 0
for i in n:
    if i == 0 and flag_0 == 0:
        count_0 += 1
        flag_0 = 1
    if i == 1:
        flag_0 = 0


if count_1 > count_0:
    print(count_0)
else:
    print(count_1)