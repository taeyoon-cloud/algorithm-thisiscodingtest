n = int(input())

arr = []

for i in range(n):
    name, grade = input().split()
    arr.append((name, int(grade)))

print(arr)


arr.sort(key=lambda x:x[1])

for student in arr:
    print(student[0], end=' ')