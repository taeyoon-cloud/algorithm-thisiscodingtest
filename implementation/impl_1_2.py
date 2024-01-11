n = int(input())

count = 0
for i in range(60):
    for j in range(60):
        if '3' in str(i) + str(j):
            count += 1


if n < 3:
    print(count * n)

elif n < 13:
    print(count * n + 3600)

elif n < 23:
    print(count * n + 7200)

else:
    print(count * n + 10800)